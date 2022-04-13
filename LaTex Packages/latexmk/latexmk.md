### Latexmk
1. 安装perl（linux或者Mac OS自带perl）
  ```python
  which perl

  /usr/bin/perl
  ```

2. 安装latexmk
  ```python
  sudo apt install latexmk

  which latexmk ---->
  /usr/bin/latexmk
  ```

3. 编译
  ```python
  latexmk -pdf -xelatex
  ```

4. 删除除tex和pdf文件之外的文件
  ```python
  latexmk -c
  ```

5. 删除除tex文件之外的文件
  ```python
  latexmk -C
  ```

6. 配置'~/.local/bin/buildchinesepdf.sh'
  ```python
  latexmk -pdf -xelatex
  #filename=$1

  #xelatex "$filename"
  ```


