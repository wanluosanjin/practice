
;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(ansi-color-names-vector
   ["black" "red3" "ForestGreen" "yellow3" "blue" "magenta3" "DeepSkyBlue" "gray50"])
 '(custom-enabled-themes (quote (light-blue)))
 '(package-archives
   (quote
    (("gnu" . "http://elpa.gnu.org/packages/")
     ("mexlpa" . "https://melpa.org/packages/")
     ("org" . "https://orgmode.org/elpa/")
     ("melpa" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/melpa/")
     ("gnu" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/gnu/"))))
 '(package-selected-packages (quote (undo-tree org))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(defalias 'yes-or-no-p 'y-or-n-p)

;;quit-window
;;简单的初始设置
;;(menu-bar-mode 0)
;(tool-bar-mode -1)

(set-frame-height (selected-frame) 30)
(setq make-backup-files nil)
(load "~/.emacs.d/init.el")

;(add-to-list 'default-frame-alist '(fullscreen . maximized))

;;也可以use-package
;;(add-hook 'after-init-hook 'global-company-mode)
;;几个键
;;(global-set-key (kbd "M-1") 'shell-command)
;;(global-set-key (kbd "M-z") 'suspend-frame)
;;(global-set-key (kbd "C-z") 'undo)



;;m+方向键不起作用
;;(global-set-key (kbd "<M-left>") 'previous-buffer)
;;(global-set-key (kbd "<M-up>") 'delete-other-windows)
;;(global-set-key (kbd "<M-down>") 'other-window)
;;(global-set-key (kbd "<M-right>") 'next-buffer)
;;completion-at-point
;;defvar
;;define-key
;;defalias
;;make-sparse-keymap
;;需要按一次cmi tab的自动补全才启动
;;(add-hook 'after-init-hook 'global-company-mode)

(global-undo-tree-mode)
(define-prefix-command 'my-prefix)
(global-set-key (kbd "<menu>") 'my-prefix)
(define-key my-prefix (kbd "n") 'myel-copy-to-next)
(global-set-key (kbd "C-`") 'delete-other-windows)
(global-set-key (kbd "C-x x") 'switch-to-next-buffer)
(global-set-key (kbd "C-x C-x") 'switch-to-prev-buffer)
;;(global-set-key [C-tab] 'other-window);;why
(global-set-key (kbd "C-w") 'kill-buffer-and-window)
(global-set-key (kbd "C-o") 'other-window)
;;(global-set-key (kbd "<M-left>") 'previous-buffer)
;;(global-set-key (kbd "<M-up>") 'delete-other-windows)
;;(global-set-key (kbd "<M-down>") 'other-window)
;;(global-set-key (kbd "<M-right>") 'next-buffer)
;;(global-set-key (kbd "C-z") 'undo)
;;(global-set-key (kbd "M-j") 'left-word)
;;(global-set-key (kbd "M-k") 'next-line)
;;(global-set-key (kbd "M-l") 'right-word)
;;(global-set-key (kbd "M-i") 'previous-line)


;C-@		set-mark-command
;C-a		move-beginning-of-line
;C-b		backward-char
;C-c		mode-specific-command-prefix
;C-d		delete-char
;C-e		move-end-of-line
;C-f		forward-char
;C-g		keyboard-quit
;C-h		help-command
;TAB		indent-for-tab-command
;C-j		electric-newline-and-maybe-indent
;C-k		kill-line
;C-l		recenter-top-bottom
;RET		newline
;C-n		next-line
;C-o		open-line
;C-p		previous-line
;C-q		quoted-insert
;C-r		isearch-backward
;C-s		isearch-forward
;C-t		transpose-chars
;C-u		universal-argument
;C-v		scroll-up-command
;C-w		kill-region
;C-x		Control-X-prefix
;C-y		yank
;C-z		suspend-frame
