Function Before_File_Name{
    $Before_File_Name = @()
    $num=0
      while ($true){
        $num++
        $Before_File_Name = (aws s3api list-objects --bucket $S3_BUCKETNAME --prefix $S3_Path --query 'Contents[].{Key: Key}' --output text)
        Write-Output $Before_File_Name | Out-Null
        #Write-Host $Before_File_Name.Count
        Write-Host $Before_File_Name[$num]
        if($null -eq $Before_File_Name[$num]){
            break
  }
 }return $Before_File_Name
}

Function Before_File_Size{
    $Before_File_Size = @()
    $num=0
      while($true){
        $num++
        $Before_File_Size = ( aws s3api list-objects --bucket $S3_BUCKETNAME --prefix $S3_Path --query 'Contents[].{Size: Size}' --output text)
        Write-Output $Before_File_Size | Out-Null
        #Write-Host $Before_File_Size.Count
        Write-Host $Before_File_Size[$num]
        if($null -eq $Before_File_Size[$num]){
            break
  }
 }return $Before_File_Size
}

Function Rename_File{
    param(
      $S3_BUCKETNAME,
      $S3_Path,
      $After_File_Name
    )
        $Before_File_Key = s3://$S3_BUCKETNAME/$S3_Path
        $After_File_Key = s3://$S3_BUCKETNAME/$After_File_Name
        $Rename_File = (aws s3 mv $Before_File_Key $After_File_Key)
        Write-Output $Rename_File | Out-Null
        return $After_File_Name
}
Function After_File_Name{
    param(
      $S3_BUCKETNAME,
      $S3_Path,
      $After_File_Name
    )
  $After_File_Name = @()
  $num=0
    while ($true){
      $num++
      $After_File_Name = (aws s3api list-objects --bucket $S3_BUCKETNAME --query 'Contents[].{Key: Key}' --output text)
      Write-Output $After_File_Name | Out-Null
      #Write-Host $Before_File_Name.Count
      Write-Host $After_File_Name[$num]
      if($null -eq $After_File_Name[$num]){
          break
  }
 }return $After_File_Name
}
  
###############################
###リネーム後のファイルサイズ取得
###############################
Function After_File_Size{
    param(
      $S3_BUCKETNAME,
      $S3_Path,
      $After_File_Name
    )
    $After_File_Size = @()
    $num=0
      while($true){
        $num++
        $After_File_Size = ( aws s3api list-objects --bucket $S3_BUCKETNAME --prefix --query 'Contents[].{Size: Size}' --output text)
        Write-Output $After_File_Size | Out-Null
        Write-Host $After_File_Size[$num]
        if($null -eq $After_File_Size[$num]){
          break
  }
 }return $After_File_Size
}

Function S3_Bucket_Check($S3_BUCKETNAME){
  $Bucket_check = (aws s3 ls --region ap-northeast-1 s3://$S3_BUCKETNAME/)
  Write-Output $Bucket_check | Out-Null
  if($null -eq $Bucket_check){
      Write-Host "S3バケット名がありません。"
      exit 1
  }
  elseif($null -ne $Bucket_check){
      Write-Host "S3バケット名があります。"
      return $S3_BUCKETNAME
  }
}

Function Compair_File(){
  param(

  )
  #filesize,filename
  
  if(<#比較対象#>){
  
  }
  if(<#比較対象#>){
  
  }  
}

Function Return_Args($return_args){
    Write-Output $Return | Out-Null
    exit 0
}
