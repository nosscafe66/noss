#Waiting状態のクラスタIDを取得する処理
Function Cluster_Check($Cluster_Name){
    #$Active_Cluster_Id = (aws emr list-clusters --active --query  "Clusters[?Name=='$Cluster_Name'].[Id]"--output text)
    while ($true){
        $Waiting_Status_Cluster = (aws emr list-clusters --cluster-states WAITING --query  "Clusters[?Name=='$Cluster_Name'].[Status.State]"--output text)
        Write-Host $Waiting_Status_Cluster
        if($Waiting_Status_Cluster -eq 'STARTING'){
            Write-Host "Cluster starting... Autocheck state 10 seconds later"
            Start-Sleep -Second 10
        }elseif($Waiting_Status_Cluster -eq 'WAITING'){
            Write-Host "Job waiting... EMR Step Start"
            break
        }
    }
    $Waiting_Cluster_Id = (aws emr list-clusters --cluster-states WAITING --query  "Clusters[?Name=='$Cluster_Name'].[Id]"--output text)
    return $Waiting_Cluster_Id
}
#Step実行処理
Function Step_Run{
    Param(
        $Test_Cluster_Id,
        $Job_Name,
        $S3_Script_path
    )
    #Write-Host "1：$Id 2：$Job_Name 3：$S3_Udf_path 4：$S3_Script_path 5：$Args1 6：$Args2 7：$Args3"
    #$Step_Run_Id = (aws emr add-steps --cluster-id $Id --steps Type=spark,Name=$Job_Name,ActionOnFailure=CONTINUE,Args=[--deploy-mode,cluster,--py-files,$S3_Udf_path,$S3_Script_path,$Args1,$Args2,$Args3])
   # {     "StepIds": [         "s-VYZUI500858M"     ] }
    $Step_Run = (aws emr add-steps --cluster-id $Test_Cluster_Id --steps Type=Spark,Name=$Job_Name,ActionOnFailure=CONTINUE,Args=[--deploy-mode,cluster,--py-files,$S3_Script_path])
    Write-Host $Step_Run
    $Step_Run_Id = (aws emr list-steps --cluster-id $Test_Cluster_Id --query "Steps[?Name=='$Job_Name'].[Id]"--output text)#成功したステップ実行command
    Write-Host $Step_Run_Id
    return $Step_Run_Id
}
#ステップ実行のポーリング処理(10秒間隔)
Function Polling_Run($Polling_Cluster_Id,$Polling_Step_Id){
    while ($true){
        $Step_Status = (aws emr describe-step --cluster-id $Polling_Cluster_Id --step-id $Polling_Step_Id --query "Step.Status.State"--output text)
        Write-Host $Step_Status
        if($Step_Status -eq 'PENDING'){
                Write-Host "Cluster creating... Autocheck state 10 seconds later"
                Start-Sleep -Second 10
            }elseif($Step_Status -eq 'RUNNING'){
                Write-Host "Job running... Autocheck state 10 seconds later"
                Start-Sleep -Second 10
            }elseif($Step_Status -eq 'FAILED'){
                Write-Host "Job failed"
                return $Step_Status
            }else{
                Write-Host "Job completed"
                return $Step_Status
            }
     }         
}
#ステップIDが取得できているかの確認
Function CheckNullOrEmpty($Cluster_Id,$Step_Id){
     if($null -eq $Step_Id){
        Write-Host "No_Step_Run"
    }
    elseif($null -ne $Step_Id){
        Start-Sleep -Second 10
        Write-Host "Starting Polling"
        $Status = Polling_Run $Cluster_Id $Step_Id
        return $Status
    }
}
#メイン処理
Function Main_Step_Start($NAME){
    $Cluster_Id = Cluster_Check $NAME
    $Step_Id = Step_Run -Test_Cluster_Id $Cluster_Id -Job_Name job_test4 -S3_Script_path make_file.py 
    #$Step_Id = "s-TLYDKQDSCUI"
    $Check = CheckNullOrEmpty $Cluster_Id $Step_Id
}
#戻り値の引き渡し
Function Return_Args($return_args){
    $Return = Main_Step_Start $return_args
    Write-Host $Return
    exit 1
}Return_Args $Args[0]
