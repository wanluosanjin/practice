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
 '(completion-styles '(flex basic partial-completion emacs22))
 '(cursor-type 'bar)
 '(custom-enabled-themes '(wheatgrass))
 '(enable-recursive-minibuffers t)
 '(ivy-mode t)
 '(ivy-use-virtual-buffers t)
 '(make-backup-files nil)
 '(marginalia-mode t)
 '(package-archives
   '(("gnu" . "http://elpa.gnu.org/packages/")
     ("mexlpa" . "https://melpa.org/packages/")
     ("org" . "https://orgmode.org/elpa/")
     ("melpa" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/melpa/")
     ("gnu" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/gnu/")))
 '(package-selected-packages
   '(company-tabnine flycheck lsp-ivy dap-mode treemacs-projectile lsp-treemacs lsp-ui lsp-mode counsel-projectile projectile dashboard use-package highlight-symbol wgrep counsel-at-point counsel-ag-popup counsel marginalia ivy-avy ivy avy which-key helm-ag helm evil undo-tree org))
 '(ring-bell-function 'ignore)
 '(tab-always-indent 'complete)
 '(undo-tree-auto-save-history nil)
 '(which-key-mode t))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(defalias 'yes-or-no-p 'y-or-n-p)


;(set-frame-height (selected-frame) 40)

(global-undo-tree-mode)
(define-prefix-command 'my-prefix)
(global-set-key (kbd "<menu>") 'my-prefix)
(define-key my-prefix (kbd "n") 'myel-copy-to-next)
(global-set-key (kbd "C-`") 'delete-other-windows)
(global-set-key (kbd "C-x x") 'switch-to-next-buffer)
(global-set-key (kbd "C-x C-x") 'switch-to-prev-buffer)
(global-set-key (kbd "C-q") 'kill-buffer-and-window)
(global-set-key (kbd "C-o") 'other-window)
(global-set-key (kbd "<M-left>") 'previous-buffer)
(global-set-key (kbd "<M-up>") 'delete-other-windows)
(global-set-key (kbd "<M-down>") 'other-window)
(global-set-key (kbd "<M-right>") 'next-buffer)
(global-set-key (kbd "<escape>") 'keyboard-escape-quit)
(global-set-key (kbd "C-c C-c") 'clipboard-kill-ring-save)
(global-set-key (kbd "C-z") 'undo-tree-undo)
(global-set-key (kbd "M-z") 'undo-tree-redo)
(global-set-key (kbd "C-v") 'clipboard-yank)

(global-set-key (kbd "C-s") 'swiper)
(global-set-key (kbd "C-x C-r") 'ivy-resume)
(global-set-key (kbd "<f6>") 'ivy-resume)
(global-set-key (kbd "M-x") 'counsel-M-x)
(global-set-key (kbd "C-x C-f") 'counsel-find-file)
(global-set-key (kbd "<f1> f") 'counsel-describe-function)
(global-set-key (kbd "<f1> v") 'counsel-describe-variable)
(global-set-key (kbd "<f1> o") 'counsel-describe-symbol)
(global-set-key (kbd "<f1> l") 'counsel-find-library)
(global-set-key (kbd "<f2> i") 'counsel-info-lookup-symbol)
(global-set-key (kbd "<f2> u") 'counsel-unicode-char)
(global-set-key (kbd "C-x g") 'counsel-git)
(global-set-key (kbd "C-x j") 'counsel-git-grep)
(global-set-key (kbd "C-x k") 'counsel-ag)
(global-set-key (kbd "C-x l") 'counsel-locate)
(global-set-key (kbd "C-S-o") 'counsel-rhythmbox)
(define-key minibuffer-local-map (kbd "C-r") 'counsel-minibuffer-history)
(define-key ivy-minibuffer-map (kbd "<C-up>") 'ivy-previous-history-element)


(define-minor-mode normal-mode
  "normal mode."
  :keymap (make-sparse-keymap))

;;(global-set-key (kbd "<escape>") 'normal-mode)
(define-prefix-command 'my-prefix)
(define-key normal-mode-map (kbd "<SPC>") 'my-prefix)
(define-key normal-mode-map (kbd "SPC SPC") 'counsel-M-x)
(define-key normal-mode-map (kbd "<escape>") 'counsel-M-x)
(define-key normal-mode-map (kbd "i") 'self-insert-command)
(define-key normal-mode-map (kbd "o") 'self-insert-command)
(define-key normal-mode-map (kbd "p") 'self-insert-command)
(define-key normal-mode-map (kbd "h") 'self-insert-command)
(define-key normal-mode-map (kbd "j") 'self-insert-command)
(define-key normal-mode-map (kbd "k") 'self-insert-command)
(define-key normal-mode-map (kbd "l") 'self-insert-command)
(define-key normal-mode-map (kbd "h") 'self-insert-command)
;; (global-set-key (kbd "i") '(lambda ()
;;         (interactive)
;;         (set-mark)))




(use-package projectile
  :ensure t
  :bind (("C-p" . projectile-command-map))
  :config
  (setq projectile-mode-line "Projectile")
  (setq projectile-track-known-projects-automatically nil))

(use-package counsel-projectile
  :ensure t
  :after (projectile)
  :init (counsel-projectile-mode))

(use-package treemacs
  :ensure t
  :defer t
  :config
  (treemacs-tag-follow-mode)
  :bind
  (:map global-map
        ("M-0"       . treemacs-select-window)
        ("C-x t 1"   . treemacs-delete-other-windows)
        ("C-x t t"   . treemacs)
        ("C-x t B"   . treemacs-bookmark)
        ;; ("C-x t C-t" . treemacs-find-file)
        ("C-x t M-t" . treemacs-find-tag))
  (:map treemacs-mode-map
	("/" . treemacs-advanced-helpful-hydra)))

(use-package treemacs-projectile
  :ensure t
  :after (treemacs projectile))

(use-package lsp-treemacs
  :ensure t
  :after (treemacs lsp))

(use-package lsp-mode
  :ensure t
  :init
  ;; set prefix for lsp-command-keymap (few alternatives - "C-l", "C-c l")
  
  (setq 
	lsp-file-watch-threshold 500)
  :hook 
  (lsp-mode . lsp-enable-which-key-integration) ; which-key integration
  :commands (lsp lsp-deferred)
  :config
  (setq lsp-completion-provider :none) ;; 阻止 lsp 重新设置 company-backend 而覆盖我们 yasnippet 的设置
  (setq lsp-headerline-breadcrumb-enable t)
  :bind
  ("C-x l" . lsp-ivy-workspace-symbol)) ;; 可快速搜索工作区内的符号（类名、函数名、变量名等）

(use-package lsp-ui
  :ensure t
  :config
  (define-key lsp-ui-mode-map [remap xref-find-definitions] #'lsp-ui-peek-find-definitions)
  (define-key lsp-ui-mode-map [remap xref-find-references] #'lsp-ui-peek-find-references)
  (setq lsp-ui-doc-position 'top))

(use-package lsp-ivy
  :ensure t
  :after (lsp-mode))

(use-package flycheck
  :ensure t
  :config
  (setq truncate-lines nil) ; 如果单行信息很长会自动换行
  :hook
  (prog-mode . flycheck-mode))

(use-package dap-mode
  :ensure t
  :after  lsp-mode
  :commands dap-debug
  :custom
  (dap-auto-configure-mode t)
  :config
  (dap-ui-mode 1))

(use-package company-tabnine
  :ensure t
  ;:init (add-to-list 'company-backends #'company-tabnine)
  )

;;quit-window
;;简单的初始设置
;;(menu-bar-mode 0)
					;(tool-bar-mode -1)

;;(load "~/.emacs.d/init.el")

;(add-to-list 'default-frame-alist '(fullscreen . maximized))

;;也可以use-package
;;(add-hook 'after-init-hook 'global-company-mode)
;;几个键
;;(global-set-key (kbd "M-1") 'shell-command)
;;(global-set-key (kbd "M-z") 'suspend-frame)
;;(global-set-key (kbd "C-z") 'undo)

;;m+方向键不起作用
;;completion-at-point
;;defvar
;;define-key
;;defalias
;;make-sparse-keymap
;;需要按一次cmi tab的自动补全才启动
;;(add-hook 'after-init-hook 'global-company-mode)

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
