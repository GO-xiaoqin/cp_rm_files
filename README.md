# cp_rm_files
这是一个python写的可以对一个文件夹下面批量的文件进行复制和删除
需求的话主要是因为工作需要遇到过类似的问题，在Linux下还是很好用的

## 下面几点注意点

* 直接把两个文件放在要复制的的目录下
* files.conf这个配置文件名是不变的，如果想要更改，可以在 .py文件里面更改
* 运行时要携带命令行参数，cp\rm两个选择，当然这个也可以在 .py文件里面更改

## 下面.conf 文件说明

* rm_files 要删除文件的序列，以逗号隔开，细节可以看 .py文件
* cp_files 要复制文件的序列，同上
* cp_or_rm_files_path 删除复制的路径，定到目录级别，要加/，因为这个是要拼接的
