gitimgbed 通过web页面展示jsDelivr加速后的github仓库中的图片。

1. 新建一个github仓库只用于存放图片
2. github->settings-> Developer settings 新建一个Personal access tokens
3. 将仓库（<user>/<仓库名>）和access tokens写到img/views.py中去
4. python3 manage.py runserver

todo:
* 复制成功有alert提示
* 图片上传