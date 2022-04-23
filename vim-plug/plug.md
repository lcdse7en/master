#### 1.NERDTree
[ scrooloose/nerdtree ](https://github.com/valsorym/scrooloose-nerdtree)
```vim
" Nerdtree U C I
nnoremap <silent> <F2> :NERDTreeToggle<ENTER>                     let NERDTreeMinimalUI=1
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && ex
ists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
```


