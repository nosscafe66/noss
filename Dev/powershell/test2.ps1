#ログ出力処理
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



#動作中のクラスタIDを取得
Function Active_ClusterId_Get($Cluster_Name){
    $Active_Cluster_Id = (aws emr list-clusters --active --query  "Clusters[?Name=='$Cluster_Name'].[Id]"--output text)
    return $Active_Cluster_Id
}


#重複チェック処理：チェック方法はクラスタ名＋ステータス（active）⇒今後実装予定
Function Double_Check($Cluster_Name,$Status_ID){
    $Cluster_Status = (aws emr list-clusters --active --query "Clusters[?Name=='$Cluster_Name']|[?Id =='$Status_ID'].[Status.State]"--output text)
    while($true){
        if($Cluster_Status -ne 'TERMINATED'){
            Write-Host "クラスター削除を行います。"
            break
        }else{
            Write-Host "同一クラスタ名での重複を確認しました。処理を終了します。"
        }
    }return $Cluster_Status
}

#クラスターの削除
Function Active_ClusterId_Delete($Terminate_Cluster_Status){
    aws emr modify-cluster-attributes --cluster-id $Active_ClusterId_Delete --no-termination-protected
    $Terminate_Cluster_Status = (aws emr terminate-clusters --cluster-id $Active_ClusterId_Delete --query 'Cluster.Status.State' --output text)
    while($true){
        if($Terminate_Cluster_Status -ne'TERMINATED'){
            Write-Host "クラスターは終了しています。"
            Start-Sleep -Second 10
        }else{
            Write-Host $Active_Cluster_Id "ユーザーのリクエストによりクラスターは削除されました。"
        }
    }return $Terminate_Cluster_Status
}

#メイン処理
Function MainTest_Stop($NAME){
    Log $LogString
    $ID = Active_ClusterId_Get $NAME
    $Status = Double_Check $NAME $ID
    Active_ClusterId_Delete $Status
}

#ジョブへの戻り値の引き渡し
Function Return_Args($return_args){
    $Return = MainTest_Stop $return_args
    Write-Host $Return
    exit 1
}Return_Args $Args[0]
