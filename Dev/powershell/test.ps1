function Log($LogString){
    # ログの出力先
    $LogPath = Convert-Path .
    $LogPath = $LogPath + "\log"
    #$LogPath = "C:\Users\R8801266\Desktop\EMR\EMR_END\test\log"

    # ログファイル名
    $LogName = "ExecutLog"
    # 日付取得
    $Now = Get-Date

    # Log 出力文字列に時刻を付加(YYYY/MM/DD HH:MM:SS.MMM $LogString)
    $Log = $Now.ToString("yyyy/MM/dd HH:mm:ss.fff") + " "
    $Log += $LogString

    # ログファイル名が設定されていなかったらデフォルトのログファイル名をつける
    if( $LogName -eq $null ){
        $LogName = "LOG"
    }

    # ログファイル名(XXXX_YYYY-MM-DD.log)
    $LogFile = $LogName + "_" +$Now.ToString("yyyy-MM-dd") + ".log"

    # ログフォルダーがなかったら作成
    if( -not (Test-Path $LogPath) ) {
        New-Item $LogPath -Type Directory
    }
    
    # ログファイル名
    $LogFileName = Join-Path $LogPath $LogFile
    
    # ログ出力
    #Write-Output $Log | Out-File -FilePath $LogFileName -Encoding Default -append
    Start-Transcript $LogFileName -append
    
    # echo させるために出力したログを戻す
    Return $Log
}

#Jsonファイル存在確認
Function Json_File_Validate($PATH){
    Test-path ("$PATH\*EMR*" + "*.json")
    #$return = Get-ChildItem -Path .\*.json
    return $return
}

#EMRクラスタ作成処理
Function Create_EMR_Cluster($Cluster_Name){
    $Cluster_Id = $null
    Write-Host $Cluster_Name
    $Cluster_Id=(aws emr create-cluster --name $Cluster_Name --release-label emr-5.32.0 --applications Name=Hadoop Name=Hive Name=Ganglia Name=Spark --ec2-attributes file://EMR1.json --instance-groups file://EMR2.json --configurations file://EMR3.json --auto-scaling-role EMR_AutoScaling_DefaultRole --termination-protected  --ebs-root-volume-size 10 --service-role EMR_DefaultRole --scale-down-behavior TERMINATE_AT_TASK_COMPLETION --region us-east-2)
    #Write-Host $Cluster_Id
    #Write-Output Starting EMR cluster ID : $Cluster_Id ...
    #aws emr wait cluster-running --cluster-id $Cluster_Id

    #以下のEMR起動オプションについては検討
    #--log-uri (string)⇒ログに関する内容
}

#メイン処理
Function Main($DIR,$NAME){
    Log $LogString
    Json_File_Validate $DIR
    If(Json_File_Validate){
        Write-Host "Verification_json_File !"
        Create_EMR_Cluster $NAME
    }
    else{
        Write-Host "None_json_File..."
        Write-Host "Stop..."
        exit
    }
}

#ジョブへの戻り値の引き渡し
Function Return_Args($return_args){
    $Return = Main (Convert-Path .) $return_args
    Write-Host $Return
    #exit 1
}Return_Args $Args[0]
