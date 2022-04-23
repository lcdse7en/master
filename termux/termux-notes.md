#### 1.Get Storage
```shell
termux-setup-storage
```

#### 2.修改启动问候语
```shell
vim $PREFIX/etc/motd
```

#### 3.自定义快捷栏
```shell
mkdir .termux
vim .termux/termux.properties

extra-keys[ \
    ['ESC','/','-','HOME','UP','END','|'], \
	['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','F5'] \
]
```

<++>
