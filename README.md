# Research-Video-Encoding<!-- omit in toc -->

## 目次<!-- omit in toc -->
- [EC2 On Demand Instance Encoding](#ec2-on-demand-instance-encoding)
    - [aws credentialsの設定](#aws-credentialsの設定)
- [EC2 Spot Instance Encoding](#ec2-spot-instance-encoding)
    - [まだやれてない😭😭😭](#まだやれてない)
- [参考資料](#参考資料)

## EC2 On Demand Instance Encoding
1. オンデマンドインスタンスを作成する
2. SSH接続する
3. EC2インスタンスにffmpegをインストールする
   ```
   sudo su - //change root user 

    cd /usr/local/bin //move dir

    mkdir ffmpeg //create dir named ffmpeg

    wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz //download ffmpeg file

    tar -xf ffmpeg-release-amd64-static.tar.xz //unpacking download file

    cd ffmpeg-6.0-amd64-static //mov unpacked file

    ./ffmpeg -version //解凍後のディレクトリファイルでしか./ffmpegコマンドは使えない
    ```
4. S3バケットにエンコードしたい動画をアップロードする
5. S3バケットからインスタンスに動画をダウンロードする
   ```
   aws s3 cp s3://[バケット名]/[ファイル名] [保存先]
   ```
   #### aws credentialsの設定
    ```
    aws configure
    ```
    ```
    AWS Access Key ID [None]: アクセスキーID
    AWS Secret Access Key [None]: シークレットアクセスキー
    Default region name [None]: リージョン名
    Default output format [None]: json
    ```
6. エンコードする
    ```
    import subprocess
    import time

    input_file = "/usr/local/bin/video_name"
    output_file = "file_name.mp4"
    resolution = "1920x1080"
    codec = "libx264"

    start_time = time.time()

    # FFmpegコマンドの作成
    ffmpeg_cmd = f"/usr/local/bin/ffmpeg-6.0-amd64-static/./ffmpeg -i {input_file} -s {resolution} -c:v {codec} {output_file}"

    # FFmpegの実行
    subprocess.call(ffmpeg_cmd, shell=True)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"エンコード時間: {elapsed_time}秒")
    ```
    #### コードの説明
    ```
    import subprocess
    import time
    ```
    - subprocessモジュールは、Pythonから外部プログラムを実行するためのモジュールです。
    - timeモジュールは、時間に関する処理を行うためのモジュールです。
    ```
    input_file = "/usr/local/bin/video_name"
    output_file = "file_name.mp4"
    resolution = "1920x1080"
    codec = "libx264"
    ```
    - input_fileは、エンコードしたい動画のパスを指定します。
    - output_fileは、エンコード後の動画のファイル名を指定します。
    - resolutionは、エンコード後の動画の解像度を指定します。
    - codecは、エンコード後の動画のコーデックを指定します。
    ```
    start_time = time.time()
    ```
    - time.time()は、プログラム実行からの経過秒数を返します。
    - start_timeは、エンコード前の時間を取得します。
    ```
    ffmpeg_cmd = f"/usr/local/bin/ffmpeg-6.0-amd64-static/./ffmpeg -i {input_file} -s {resolution} -c:v {codec} {output_file}"
    ```
    - ffmpeg_cmdは、FFmpegコマンドを作成します。
    ```
    subprocess.call(ffmpeg_cmd, shell=True)
    ```
    - subprocess.call()は、引数に指定したコマンドを実行します。
    ```
    end_time = time.time()
    elapsed_time = end_time - start_time
    ```
    - end_timeは、エンコード後の時間を取得します。
    - elapsed_timeは、エンコード時間を計算します。
    ```
    print(f"エンコード時間: {elapsed_time}秒")
    ```
    - print()は、引数に指定した文字列を出力します。

## EC2 Spot Instance Encoding
#### まだやれてない😭😭😭

## 参考資料
- [EC2内にFFmpegをインストールしてAWS MediaPackageのエンドポイントからMP4ファイルを作成する方法](https://www.monster-dive.com/blog/web_system/20210209_002010.php)

[def]: #参考資料
