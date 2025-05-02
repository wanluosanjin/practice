
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
   ["black" "red3" "ForestGreen" "yellow3" "blue" "magenta3"
    "DeepSkyBlue" "gray50"])
 '(completion-styles '(flex basic partial-completion emacs22))
 '(cursor-type 'hbar)
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
   '(company-tabnine flycheck lsp-ivy dap-mode treemacs-projectile
		     lsp-treemacs lsp-ui lsp-mode counsel-projectile
		     projectile dashboard use-package highlight-symbol
		     wgrep counsel-at-point counsel-ag-popup counsel
		     marginalia ivy-avy ivy avy which-key helm-ag helm
		     evil undo-tree org))
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

(global-undo-tree-mode)

;(set-frame-height (selected-frame) 40)


(global-set-key (kbd "C-`") 'delete-other-windows)
(global-set-key (kbd "C-x C-x") 'set-mark-command)
(global-set-key (kbd "C-q") 'femacs-mode)
(global-set-key (kbd "C-o") 'avy-goto-char-timer)
(global-set-key (kbd "<M-left>") 'previous-buffer)
(global-set-key (kbd "<M-up>") 'delete-other-windows)
(global-set-key (kbd "<M-down>") 'other-window)
(global-set-key (kbd "<M-right>") 'next-buffer)
(global-set-key (kbd "<escape>") 'keyboard-quit)
(global-set-key (kbd "C-c C-c") 'clipboard-kill-ring-save)
(global-set-key (kbd "C-z") 'undo-tree-undo)
(global-set-key (kbd "M-z") 'undo-tree-redo)
(global-set-key (kbd "C-v") 'clipboard-yank)
(global-set-key (kbd "C-;") 'end-of-buffer)
(global-set-key (kbd "C-:") 'beginning-of-buffer)

(global-set-key (kbd "C-s") 'swiper-thing-at-point)
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;femacs

(define-minor-mode femacs-mode
  "femacs-mode."
  :global t
  :keymap (make-sparse-keymap))
(femacs-mode nil)
(define-key femacs-mode-map (kbd "C-q") 'kill-buffer-and-window)
(define-key femacs-mode-map (kbd "u") 'previous-buffer)
(define-key femacs-mode-map (kbd "p") 'next-buffer)


(defun forward-select (move-fn)
  "Perform MOVE-FN with proper region expansion handling."
  (if (use-region-p)
      (let ((point-is-after-mark (< (point) (mark))))
        (if point-is-after-mark
            (exchange-point-and-mark))) ;; make point before mark
    )
  (funcall move-fn))
(defun backward-select (move-fn)
  "Perform MOVE-FN with proper region expansion handling."
  (if (use-region-p)
      (let ((point-is-before-mark (> (point) (mark))))
        (if point-is-before-mark
            (exchange-point-and-mark))) ;; make point before mark
    )
  (funcall move-fn))

(defun smart-forward-word ()
  "."
  (interactive)
       (forward-select #'right-word))

(defun smart-backward-word ()
  "."
  (interactive)
  (backward-select #'left-word))

(defun move-to-previous-bol ()
  "Move cursor to the beginning of the previous line."
  (interactive)
  (forward-char -1)
  (beginning-of-line))
(defun move-to-next-eol ()
  "Move cursor to the end of the next line."
  (interactive)
  (forward-char 1)
  (end-of-line))
(defun smart-next-line ()
  "."
  (interactive)
  (forward-select #'move-to-next-eol))

(defun smart-previous-line ()
  "."
  (interactive)
 (backward-select #'move-to-previous-bol))
(define-key femacs-mode-map (kbd "h") 'smart-backward-word)
(define-key femacs-mode-map (kbd "k") 'smart-previous-line)
(define-key femacs-mode-map (kbd "j") 'smart-next-line)
(define-key femacs-mode-map (kbd "l") 'smart-forward-word)
(define-key femacs-mode-map (kbd "n") 'my-scroll-up-half-page-keep-cursor)
(define-key femacs-mode-map (kbd "m") 'my-scroll-down-half-page-keep-cursor)

;;;;;;;;;;;;;;;;;;;;;;;;my-menu
(define-prefix-command 'femacs-prefix)
(global-set-key (kbd "<menu>") 'femacs-prefix)
(define-key femacs-prefix (kbd "n") 'myel-copy-to-next)
(define-key femacs-prefix (kbd "<menu>") 'femacs-mode)

;;;;;;;;;;;;;;;;;;;;;;;space
(define-prefix-command 'femacs-space-prefix)
(define-key femacs-mode-map (kbd "<SPC>") 'femacs-space-prefix)
(define-key femacs-mode-map (kbd "SPC SPC") 'counsel-M-x)

;;;;;;;;;;;;;;;;;;;;;;;o-i
(define-prefix-command 'femacs-o-prefix)
(define-key femacs-mode-map (kbd "o") 'femacs-o-prefix)
(define-key femacs-mode-map (kbd "o i") 'femacs-mode)
(define-key femacs-mode-map (kbd "o o") 'avy-goto-char-timer)

(define-key femacs-mode-map (kbd "i") 'smart-expand-region)

;; (define-prefix-command 'femacs-i-prefix)
;; (define-key femacs-mode-map (kbd "i") 'femacs-i-prefix)
;; (define-key femacs-i-prefix (kbd "i") 'mark-whole-sexp)
;; (defun femacs-mark-whole-line ()
;;   "Select the current line."
;;   (interactive)
;;   (beginning-of-line)
;;   (set-mark (line-end-position)))
;; (define-key femacs-i-prefix (kbd "l") 'femacs-mark-whole-line)


;;;;;;;;;;;;;;;;;;;;mini-buffer
(setq femacs-mode-before-minibuffer femacs-mode)
(defun femacs-minibuffer-setup ()
  "Cancel femacsmode."
  (setq femacs-mode-before-minibuffer femacs-mode)
  (if femacs-mode
      (femacs-mode 0)
      nil))
;;(call-interactively 'femacs-mode t (vector 1)) no need to use
(defun femacs-minibuffer-exit ()
  "Recover femacsmode."
  (femacs-mode (if femacs-mode-before-minibuffer 1 0)))
(add-hook 'minibuffer-setup-hook #'femacs-minibuffer-setup 'local)

(add-hook 'minibuffer-exit-hook #'femacs-minibuffer-exit 'local)

(defun femacs-mode-esc ()
  "Esc to femacsmode."
  (interactive)
  (if femacs-mode
      (keyboard-escape-quit)
    (call-interactively 'femacs-mode)))

(defun mark-whole-sexp ()
  "."
  (interactive)
  (let ((bound (bounds-of-thing-at-point 'sexp)))
    (if bound
        (progn
          (goto-char (car bound))
          (set-mark (point))
          (goto-char (cdr bound)))
      (message "No sexp found at point!"))))


;; (defmacro once-only ((&rest names) &body body)
;;      (let ((gensyms (loop for n in names collect (gensym))))
;;        `(let (,@(loop for g in gensyms collect `(,g (gensym))))
;;          `(let (,,@(loop for g in gensyms for n in names collect ``(,,g ,,n)))
;;            ,(let (,@(loop for n in names for g in gensyms collect `(,n ,g)))
;;               ,@body)))))

;; (defmacro square (x)
;;   (once-only (x)
;;     `(* ,x ,x)))
;; https://oneforalone.github.io/lol-zh/chapter03.html




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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
  
  (setq lsp-file-watch-threshold 500)
  :hook (lsp-mode . lsp-enable-which-key-integration) ; which-key integration
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
;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with ‘<open>’ and enter text in its buffer.

(defun smart-expand-region ()
  "Expand region progressively: word → sexp → sentence → page.
Each time you call, the region will grow based on thing-at-point boundaries."
  (interactive)
  ;; 初次调用：设置 mark
  (catch 'done
    (unless (my-use-region-p)
      (set-mark-command nil)
      (message "Set mark.")
      (throw 'done nil))
    (let ((start (region-beginning))
          (end (region-end)))

      (dolist (thing '(word symbol number filename url email uuid whitespace line list sexp defun  sentence page))
        (let ((bounds (bounds-of-thing-at-point thing)))
          (when (and bounds
                    (>= start (car bounds))
                    (<= end (cdr bounds))
                    (not (and (= start (car bounds))
                              (= end (cdr bounds)))))
            (set-mark (car bounds))
            (goto-char (cdr bounds))
            (message "Selected: %s" thing)
            (throw 'done nil))))
      ;; 当前为 page，重置回 word
      (let ((page (bounds-of-thing-at-point 'page)))
        (when (and page
                  (= start (car page))
                  (= end (cdr page)))
              (set-mark-command nil)
              (message "Set mark.")))))
)
(defun my-use-region-p ()
  "."
  (and (mark) (region-active-p)))



(defun my-scroll-down-half-page-keep-cursor ()
  "Scroll down half a page while keeping point's relative position in the window."
  (interactive)
  (let* ((current-line (count-screen-lines (window-start) (point)))
         (half-page (max 1 (/ (window-body-height) 2))))
    (scroll-down-command half-page)
    (move-to-window-line current-line)))


(defun my-scroll-up-half-page-keep-cursor ()
  "Scroll up half a page while keeping point's relative position in the window."
  (interactive)
  (let* ((current-line (count-screen-lines (window-start) (point)))
         (half-page (max 1 (/ (window-body-height) 2))))
    (scroll-up-command half-page)
    (move-to-window-line current-line)))



