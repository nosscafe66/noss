#一括リネーム処理

#aws s3 ls s3://fj-ndb3-com/ndb/ --recursive --human-readable --sum | Select-String "Total Size" | % { $($_ -split ",") } | % { $_.TrimStart() } (トータルバケット数取得)
#aws s3 ls s3://fj-ndb3-com/ndb/ --recursive --human-readable --sum | Select-String "Total Objects:" | % { $($_ -split ",") } | % { $_.TrimStart() } (トータルオブジェクト数取得)
#aws s3api list-objects --bucket fj-ndb3-com --query 'Contents[].{Key: Key, Size: Size}' --output text (ファイル名とサイズの取得)
#aws s3api list-objects --bucket fj-ndb3-com --output text --query "[length(Contents[])]"
#aws s3api list-objects --bucket fj-ndb3-com --prefix "ndb/TestRename/" --output json --query "[length(Contents[])]" (特定フォルダの場合)
#aws s3api list-objects --bucket fj-ndb3-com --prefix /ndb/TestRename --query 'sort_by(Contents[],&LastModified)|[-1]' 最新のファイルだけを取得する

<#--exclude '*' --include '*temp*'#>

<#リターンコードの説明
exit 0 : リネームが完了し処理が正常に終わった場合
exit 1 : S3バケット名が存在しない場合


#>

############################
###リネーム前のファイル名取得
############################
Function Before_File_Name{
<#後程引数として使用する
    param(
      $S3_BUCKETNAME,
      $S3_Path #(リネーム前のファイルまでのフルパス)
    )
    #>
    $Before_File_Name = @()
    $num=0
      while ($true){
        $num++
        Write-Host $num #後で削除
        $Before_File_Name = (aws s3api list-objects --bucket fj-ndb3-com <#$S3_BUCKETNAME#> --prefix 'ndb/TestRename/'<#$S3_Path#> --query 'Contents[].{Key: Key}' --output text) #コメントアウトの部分は後程引数となる。
        Write-Output $Before_File_Name | Out-Null
        #Write-Host $Before_File_Name.Count
        Write-Host $Before_File_Name[$num]
        if($null -eq $Before_File_Name[$num]){
            break
  }
 }return $Before_File_Name
}

###############################
###リネーム前のファイルサイズ取得
###############################
Function Before_File_Size{
<#後程引数として使用する
  param(
    $S3_BUCKETNAME,
    $S3_Path #(リネーム前のファイルまでのフルパス)
  )
  #>
    $Before_File_Size = @()
    $num=0
      while($true){
        $num++
        Write-Host $num #後で削除
        $Before_File_Size = ( aws s3api list-objects --bucket fj-ndb3-com <#$S3_BUCKETNAME#> --prefix 'ndb/TestRename/'<#$S3_Path#> --query 'Contents[].{Size: Size}' --output text) #コメントアウトの部分は後程引数となる。
        Write-Output $Before_File_Size | Out-Null
        #Write-Host $Before_File_Size.Count
        Write-Host $Before_File_Size[$num]
        if($null -eq $Before_File_Size[$num]){
            break
  }
 }return $Before_File_Size
}

#上部リネーム前情報- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



<#
##################
###ファイルカウント
##################
Function File_Count(){
  aws s3api list-objects --bucket fj-ndb3-com --prefix "ndb/TestRename/" --output text --query "[length(Contents[])]"
}
#>


###############
###リネーム処理
###############
Function Rename_File{
    param(
      $S3_BUCKETNAME,
      $S3_Path, #(リネーム前のファイルまでのフルパス)
      $After_File_Name #(リネーム後のファイル名)
    )
        $Before_File_Key = s3://$S3_BUCKETNAME/$S3_Path
        $After_File_Key = s3://$S3_BUCKETNAME/$After_File_Name
        $Rename_File = (aws s3 mv $Before_File_Key $After_File_Key)　#from to 
        Write-Output $Rename_File | Out-Null
        return $After_File_Name
}


############################
###リネーム後のファイル名取得
############################
Function After_File_Name{
<#後程引数として使用する
  param(
    $S3_BUCKETNAME,
    $S3_Path,
    $After_File_Name
  )
  #>
  $After_File_Name = @()
  $num=0
    while ($true){
      $num++
      Write-Host $num #後で削除
      $After_File_Name = (aws s3api list-objects --bucket fj-ndb3-com <#$S3_BUCKETNAME#> --query 'Contents[].{Key: Key}' --output text) #コメントアウトの部分は後程引数となる。
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
<#後程引数として使用する
    param(
      $S3_BUCKETNAME,
      $S3_Path,
      $After_File_Name
    )
    #>
    $After_File_Size = @()
    $num=0
      while($true){
        $num++
        Write-Host $num #後で削除
        $After_File_Size = ( aws s3api list-objects --bucket fj-ndb3-com <#$S3_BUCKETNAME#> --prefix --query 'Contents[].{Size: Size}' --output text) #コメントアウトの部分は後程引数となる。
        Write-Output $After_File_Size | Out-Null
        #Write-Host $After_File_Size.Count
        Write-Host $After_File_Size[$num]
        if($null -eq $After_File_Size[$num]){
          break
  }
 }return $After_File_Size
}
  
#上部リネーム後情報- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


###############--------------------------------------------------------------なくてもいい処理
#S3_バケット確認
###############
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

######################################----------------------------------------------------------------------これから記述する----------------------------------------------------------------------
###リネーム前とリネーム後のファイルの比較
######################################
Function Compair_File(){
  param(

  )
  #filesize,filename
  
  if(<#比較対象#>){
  
  }
  if(<#比較対象#>){
  
  }  
}

###########################
###ジョブへの戻り値の引き渡し
###########################
Function Return_Args($return_args){
    Write-Output $Return | Out-Null
    exit 0
}

############　想定引数(S3バケット名、S3パス、リネーム予定のファイル名)
###メイン処理
############
Function Main($S3_BUCKETNAME,$S3_Path,$After_File_Name){
  #S3_Bucket_Check $S3_BUCKETNAME #なくてもよい

  #リネーム前のファイル名とサイズ
  $Before_File_Size = Before_File_Size $S3_BUCKETNAME $S3_Path
  $Before_File_Name = Before_File_Name $S3_BUCKETNAME $S3_Path

  #リネーム処理
  Rename_File


  #リネーム後のファイル名とサイズ
  After_File_Name
  After_File_Size


  Compair_File 
}





<#


ファイル名もそうだがIDで比較することもいいのではないか？
aws s3api list-objects --bucket fj-ndb3-com --prefix 'ndb/TestRename/test4.txt' --query 'Contents[].[Owner.ID]' --output text
リネーム後と前で情報は特に何も変化なし。ファイル名のみが変化する。名前が変わるだけなのでオブジェクトとしては同じもの？
PS C:\Users\R96000494\desktop\2021_0430> aws s3api list-objects --bucket fj-ndb3-com --prefix 'ndb/TestRename/test3.txt' --query 'Contents[]' --output jsonリネーム前
[
    {
        "LastModified": "2021-04-30T03:23:07.000Z",
        "ETag": "\"7df3fcdc45b7e8790951098bdb9352a6\"",
        "StorageClass": "STANDARD",
        "Key": "ndb/TestRename/test3.txt",
        "Owner": {
            "DisplayName": "fj-aws100115",
            "ID": "c8d4420ec709d480aa2f81211e52d6376d480aaa795412159047373a5def9337"
        },
        "Size": 26
    }
]
PS C:\Users\R96000494\desktop\2021_0430> aws s3 mv s3://fj-ndb3-com/ndb/TestRename/test3.txt s3://fj-ndb3-com/ndb/TestRename/test4.txt
C:\Program Files\Amazon\AWSCLI\.\dateutil\parser\_parser.py:1189: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
move: s3://fj-ndb3-com/ndb/TestRename/test3.txt to s3://fj-ndb3-com/ndb/TestRename/test4.txt
PS C:\Users\R96000494\desktop\2021_0430> aws s3api list-objects --bucket fj-ndb3-com --prefix 'ndb/TestRename/test4.txt' --query 'Contents[]' --output jsonリネーム後
[
    {
        "LastModified": "2021-04-30T07:59:09.000Z",
        "ETag": "\"7df3fcdc45b7e8790951098bdb9352a6\"",
        "StorageClass": "STANDARD",
        "Key": "ndb/TestRename/test4.txt",
        "Owner": {
            "DisplayName": "fj-aws100115",
            "ID": "c8d4420ec709d480aa2f81211e52d6376d480aaa795412159047373a5def9337"
        },
        "Size": 26
    }
]






#>>
