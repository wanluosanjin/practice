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
 '(auto-save-default nil)
 '(completion-styles '(flex basic partial-completion emacs22))
 '(cursor-type 'hbar)
 '(custom-enabled-themes '(leuven-dark))
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
   '(avy company-tabnine counsel counsel-ag-popup counsel-at-point
	 counsel-projectile dap-mode dashboard evil expand-region
	 expreg flycheck helm helm-ag highlight-symbol ivy ivy-avy
	 lsp-ivy lsp-mode lsp-treemacs lsp-ui marginalia org
	 projectile slime treemacs-projectile undo-tree use-package
	 wgrep))
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
(setq inferior-lisp-program "/opt/homebrew/bin/sbcl")
(setq slime-contribs '(slime-fancy))
;(set-frame-height (selected-frame) 40)

;;将C-改为M-
;;(global-set-key (kbd "RET") 'femacs-mode)
(global-set-key (kbd "`") 'femacs-esc-to-femacs)
(global-set-key (kbd "C-x C-x") 'kill-region)
(global-set-key (kbd "C-q") 'kill-buffer-and-window)
(global-set-key (kbd "C-o") 'femacs-mode)
(global-set-key (kbd "C-`") 'delete-other-windows)
(global-set-key (kbd "C-j") 'avy-goto-char-timer)

(global-set-key (kbd "<escape>") 'keyboard-escape-quit);;控制行默认C-【是M的粘粘键
;;(set-quit-char ?\e) ;; 让 ESC = C-g
(global-set-key (kbd "C-c C-c") 'clipboard-kill-ring-save)
(global-set-key (kbd "C-z") 'undo-tree-undo)
(global-set-key (kbd "M-z") 'undo-tree-redo)
(global-set-key (kbd "C-v") 'clipboard-yank)
(global-set-key (kbd "C-;") 'end-of-buffer)
(global-set-key (kbd "C-:") 'beginning-of-buffer)
(global-set-key (kbd "<M-left>") 'previous-buffer)
(global-set-key (kbd "<M-up>") 'delete-other-windows)
(global-set-key (kbd "<M-down>") 'other-window)
(global-set-key (kbd "<M-right>") 'next-buffer)
(global-set-key (kbd "M-x") 'counsel-M-x)
(global-set-key (kbd "C-s") 'save-buffer)
(global-set-key (kbd "C-f") 'swiper-thing-at-point)
(global-set-key (kbd "C-w") 'backward-kill-word)
;; C-l → 重新加载配置（.emacs / init.el）
(global-set-key (kbd "C-L")
  (lambda ()
    (interactive)
    (restart-emacs)))

;; C-p → 打开 .emacs / init.el
(global-set-key (kbd "C-l")
  (lambda ()
    (interactive)
    (find-file user-init-file)))




(global-set-key (kbd "C-r") 'ivy-resume)
(global-set-key (kbd "C-b") 'ivy-switch-buffer)
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
(global-set-key (kbd "<delete>") #'femacs-esc-to-femacs)
(global-set-key (kbd "<deletechar>") #'femacs-esc-to-femacs)
(global-set-key (kbd "C-<delete>") #'femacs-esc-to-femacs)
;;ivy swiper hot key down below




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;femacs
(defun mymode-set-mode-line-color ()
  (set-face-background 'mode-line "#888888"))

(defun mymode-reset-mode-line-color ()
  (set-face-background 'mode-line nil)) ; 恢复默认


(define-minor-mode femacs-mode
  "femacs-mode."
  :global t
  :keymap (make-sparse-keymap)
  (if femacs-mode
      (mymode-set-mode-line-color)
    (mymode-reset-mode-line-color)))
(femacs-mode nil)

(defun disable-keys-in-femacs (map)
  "将常用的字母、数字、功能键在指定的 keymap 中设为无动作。"
  (let ((i 32))
    (while (< i 128)
      ;; 将数字转为字符串形式的按键，如 (kbd "a") 或直接使用向量
      (define-key map (vector i) 'ignore)
      (setq i (1+ i))))
  ;; 4. 映射功能键 F1 到 F12
  (dotimes (i 12)
    (define-key map (kbd (format "<f%d>" (1+ i))) 'ignore))
  ;; 5. 映射几个常用的特殊按键 (可根据需要增删)
  (let ((special-keys '("<return>" "<tab>" "<escape>" "<backspace>" "<delete>")))
    (dolist (key special-keys)
      (define-key map (kbd key) 'ignore))))
(disable-keys-in-femacs femacs-mode-map)

(defun femacs-move (move-func &optional shift)
  "增强版移动代理。
实现逻辑：若按下 Shift 且移动方向导致缩选，则自动交换 point 和 mark 以保证始终为扩选。"
  (interactive)
  (if shift
      (progn
        (unless (region-active-p)
          (push-mark nil t t))
        
        ;; 核心逻辑：预测移动方向并处理“反向扩选”
        (let ((current-pos (point))
              (mark-pos (mark))
              (next-pos (save-excursion 
                          (call-interactively move-func) 
                          (point))))
          
          ;; 如果当前光标在 mark 之后(向下/右选)，但移动后位置变小了(向上/左移)
          ;; 且移动后的位置跨越了 mark，或者正在缩减选区
          (when (region-active-p)
            (cond
             ;; 情况 A: 光标在 mark 右侧，但准备向左移动（可能缩选）
             ((and (> current-pos mark-pos) (< next-pos current-pos))
              (goto-char mark-pos)
              (set-mark current-pos))
             
             ;; 情况 B: 光标在 mark 左侧，但准备向右移动（可能缩选）
             ((and (< current-pos mark-pos) (> next-pos current-pos))
              (goto-char mark-pos)
              (set-mark current-pos)))))
        
        ;; 执行实际移动
        (call-interactively move-func))
    
    ;; 未按下 Shift：取消选区并正常移动
    (when (region-active-p)
      (deactivate-mark))
    (call-interactively move-func)))


(defun femacs-w () (interactive) (femacs-move 'previous-line nil))
(defun femacs-s () (interactive) (femacs-move 'next-line nil))
(defun femacs-a () (interactive) (femacs-move 'backward-char nil))
(defun femacs-d () (interactive) (femacs-move 'forward-char nil))

(defun femacs-W () (interactive) (femacs-move 'previous-line t))
(defun femacs-S () (interactive) (femacs-move 'next-line t))
(defun femacs-A () (interactive) (femacs-move 'backward-char t))
(defun femacs-D () (interactive) (femacs-move 'forward-char t))

(defun femacs-j () (interactive) (femacs-move 'femacs-move-to-next-eol nil ))
(defun femacs-k () (interactive) (femacs-move 'femacs-move-to-previous-bol nil ))
(defun femacs-l () (interactive) (femacs-move 'forward-word nil )) 
(defun femacs-h () (interactive) (femacs-move 'backward-word nil )) 

;; 大写：选择模式
(defun femacs-J () (interactive) (femacs-move 'femacs-move-to-next-eol t ))
(defun femacs-K () (interactive) (femacs-move 'femacs-move-to-previous-bol t ))
(defun femacs-L () (interactive) (femacs-move 'forward-word t ))
(defun femacs-H () (interactive) (femacs-move 'backward-word t ))

(defun femacs-next-bracket ()
  "光标移动到下一个大中小括号。"
  (interactive)
  (re-search-forward "[][(){}]" nil t))

(defun femacs-previous-bracket ()
  "光标移动到上一个大中小括号。"
  (interactive)
  (re-search-backward "[][(){}]" nil t))

;; 绑定到 [ 和 ] 键

(defun femacs-lb () (interactive) (femacs-move 'femacs-previous-bracket nil ))
(defun femacs-rb () (interactive) (femacs-move 'femacs-next-bracket nil ))

(defun femacs-LB () (interactive) (femacs-move 'femacs-previous-bracket t ))
(defun femacs-RB () (interactive) (femacs-move 'femacs-next-bracket t ))


(define-key femacs-mode-map (kbd " ") 'ignore)
(define-key femacs-mode-map (kbd "!") 'ignore)
(define-key femacs-mode-map (kbd "\"") 'ignore)
(define-key femacs-mode-map (kbd "#") 'ignore)
(define-key femacs-mode-map (kbd "$") 'ignore)
(define-key femacs-mode-map (kbd "%") 'ignore)
(define-key femacs-mode-map (kbd "&") 'ignore)
(define-key femacs-mode-map (kbd "'") 'ignore)
(define-key femacs-mode-map (kbd "(") 'ignore)
(define-key femacs-mode-map (kbd ")") 'ignore)
(define-key femacs-mode-map (kbd "*") 'ignore)
(define-key femacs-mode-map (kbd "+") 'ignore)
(define-key femacs-mode-map (kbd ",") 'ignore)
(define-key femacs-mode-map (kbd "-") 'ignore)
(define-key femacs-mode-map (kbd ".") 'ignore)
(define-key femacs-mode-map (kbd "/") 'ignore)
(define-key femacs-mode-map (kbd "0") 'ignore)
(define-key femacs-mode-map (kbd "1") 'ignore)
(define-key femacs-mode-map (kbd "2") 'ignore)
(define-key femacs-mode-map (kbd "3") 'ignore)
(define-key femacs-mode-map (kbd "4") 'ignore)
(define-key femacs-mode-map (kbd "5") 'ignore)
(define-key femacs-mode-map (kbd "6") 'ignore)
(define-key femacs-mode-map (kbd "7") 'ignore)
(define-key femacs-mode-map (kbd "8") 'ignore)
(define-key femacs-mode-map (kbd "9") 'ignore)
(define-key femacs-mode-map (kbd ":") 'ignore)
(define-key femacs-mode-map (kbd "\;") 'ignore)
(define-key femacs-mode-map (kbd "<") 'ignore)
(define-key femacs-mode-map (kbd "=") 'ignore)
(define-key femacs-mode-map (kbd ">") 'ignore)
(define-key femacs-mode-map (kbd "?") 'ignore)
(define-key femacs-mode-map (kbd "@") 'ignore)
(define-key femacs-mode-map (kbd "A") 'femacs-A)
(define-key femacs-mode-map (kbd "B") 'ignore)
(define-key femacs-mode-map (kbd "C") 'ignore)
(define-key femacs-mode-map (kbd "D") 'femacs-D)
(define-key femacs-mode-map (kbd "E") 'ignore)
(define-key femacs-mode-map (kbd "F") 'ignore)
(define-key femacs-mode-map (kbd "G") 'ignore)
(define-key femacs-mode-map (kbd "H") 'femacs-H)
(define-key femacs-mode-map (kbd "I") 'ignore)
(define-key femacs-mode-map (kbd "J") 'femacs-J)
(define-key femacs-mode-map (kbd "K") 'femacs-K)
(define-key femacs-mode-map (kbd "L") 'femacs-L)
(define-key femacs-mode-map (kbd "M") 'ignore)
(define-key femacs-mode-map (kbd "N") 'ignore)
(define-key femacs-mode-map (kbd "O") 'ignore)
(define-key femacs-mode-map (kbd "P") 'ignore)
(define-key femacs-mode-map (kbd "Q") 'ignore)
(define-key femacs-mode-map (kbd "R") 'ignore)
(define-key femacs-mode-map (kbd "S") 'femacs-S)
(define-key femacs-mode-map (kbd "T") 'ignore)
(define-key femacs-mode-map (kbd "U") 'ignore)
(define-key femacs-mode-map (kbd "V") 'ignore)
(define-key femacs-mode-map (kbd "W") 'femacs-W)
(define-key femacs-mode-map (kbd "X") 'ignore)
(define-key femacs-mode-map (kbd "Y") 'ignore)
(define-key femacs-mode-map (kbd "Z") 'ignore)
(define-key femacs-mode-map (kbd "[") 'femacs-lb)
(define-key femacs-mode-map (kbd "\\") 'ignore)
(define-key femacs-mode-map (kbd "]") 'femacs-rb)
(define-key femacs-mode-map (kbd "^") 'ignore)
(define-key femacs-mode-map (kbd "_") 'ignore)
(define-key femacs-mode-map (kbd "`") 'ignore)
(define-key femacs-mode-map (kbd "a") 'femacs-a)
(define-key femacs-mode-map (kbd "b") 'ignore)
(define-key femacs-mode-map (kbd "c") 'ignore)
(define-key femacs-mode-map (kbd "d") 'femacs-d)
(define-key femacs-mode-map (kbd "e") 'ignore)
(define-key femacs-mode-map (kbd "f") 'ignore)
(define-key femacs-mode-map (kbd "g") 'avy-goto-char-timer)
(define-key femacs-mode-map (kbd "h") 'femacs-h)
(define-key femacs-mode-map (kbd "i") 'ignore)
(define-key femacs-mode-map (kbd "j") 'femacs-j)
(define-key femacs-mode-map (kbd "k") 'femacs-k)
(define-key femacs-mode-map (kbd "l") 'femacs-l)
(define-key femacs-mode-map (kbd "m") 'ignore)
(define-key femacs-mode-map (kbd "n") 'ignore)
(define-key femacs-mode-map (kbd "o") 'ignore)
(define-key femacs-mode-map (kbd "p") 'ignore)
(define-key femacs-mode-map (kbd "q") 'ignore)
(define-key femacs-mode-map (kbd "r") 'ignore)
(define-key femacs-mode-map (kbd "s") 'femacs-s)
(define-key femacs-mode-map (kbd "t") 'ignore)
(define-key femacs-mode-map (kbd "u") 'ignore)
(define-key femacs-mode-map (kbd "v") 'scroll-up-command)
(define-key femacs-mode-map (kbd "w") 'femacs-w)
(define-key femacs-mode-map (kbd "x") 'ignore)
(define-key femacs-mode-map (kbd "y") 'ignore)
(define-key femacs-mode-map (kbd "z") 'ignore)
(define-key femacs-mode-map (kbd "{") 'femacs-LB)
(define-key femacs-mode-map (kbd "|") 'ignore)
(define-key femacs-mode-map (kbd "}") 'femacs-RB)
(define-key femacs-mode-map (kbd "~") 'ignore)



(define-key femacs-mode-map (kbd "RET") 'femacs-scroll-up-half-page-keep-cursor)
(define-key femacs-mode-map (kbd "DEL") 'femacs-scroll-down-half-page-keep-cursor)
(define-key femacs-mode-map (kbd "c") 'clipboard-kill-ring-save)
;;(define-key femacs-mode-map (kbd "g") 'other-window)
;;(define-key femacs-mode-map (kbd "f") 'swiper-thing-at-point)
(define-key femacs-mode-map (kbd "u") 'previous-buffer)
(define-key femacs-mode-map (kbd "p") 'next-buffer)
(define-key femacs-mode-map (kbd "h") 'femacs-backward-word)
(define-key femacs-mode-map (kbd "k") 'femacs-previous-line)
(define-key femacs-mode-map (kbd "j") 'femacs-next-line)
(define-key femacs-mode-map (kbd "l") 'femacs-forward-word)
(define-key femacs-mode-map (kbd "w") 'previous-line)
(define-key femacs-mode-map (kbd "a") 'left-char)
(define-key femacs-mode-map (kbd "s") 'next-line)
(define-key femacs-mode-map (kbd "d") 'right-char)
;;(define-key femacs-mode-map (kbd "SPC") 'scroll-up-command)
(define-key femacs-mode-map (kbd "b") 'scroll-down-command)
(define-key femacs-mode-map (kbd ",") 'scroll-right)
(define-key femacs-mode-map (kbd ".") 'scroll-left)
(define-key femacs-mode-map (kbd "C-o") 'femacs-RET)
(define-key femacs-mode-map (kbd "C-d") 'femacs-DEL)
(define-key femacs-mode-map (kbd "`") 'femacs-esc-to-femacs)
(define-key femacs-mode-map (kbd "i") 'er/expand-region)
(define-key femacs-mode-map (kbd "TAB") #'other-window)
(define-key femacs-mode-map (kbd "q") #'switch-to-prev-buffer)
(define-key femacs-mode-map (kbd "e") #'switch-to-next-buffer)           


;;fffttt
(defvar femacs-last-search-text nil
  "上一次用于 f 搜索的文本")

(defun femacs-search-forward ()
  (interactive)
  (cond
   ;; 有选中文本：保存并向下搜索
   ((use-region-p)
    (let ((text (buffer-substring-no-properties
                 (region-beginning)
                 (region-end))))
      (setq femacs-last-search-text text)
      (deactivate-mark)
      (search-forward text nil nil 1)
      (set-mark (- (point) (length text)))))

   ;; 无选中，但有历史搜索文本
   (femacs-last-search-text
    (search-forward femacs-last-search-text nil nil 1)
    (set-mark (- (point) (length femacs-last-search-text))))

   ;; 都没有，给出提示
   (t
    (message "没有可搜索的文本"))))
(define-key femacs-mode-map (kbd "f") #'femacs-search-forward)


;;femacs-menu
(define-prefix-command 'femacs-menu-prefix)
(global-set-key (kbd "<menu>") 'femacs-menu-prefix)
(define-key femacs-menu-prefix (kbd "<menu>") 'femacs-mode)


;;space
;(define-prefix-command 'femacs-space-prefix)
;(define-key femacs-mode-map (kbd "<SPC>") 'femacs-space-prefix)
;(define-key femacs-mode-map (kbd "SPC SPC") nil)

;;o-i
(define-prefix-command 'femacs-o-prefix)
(define-key femacs-mode-map (kbd "o") 'femacs-o-prefix)
(define-key femacs-mode-map (kbd "o j") 'avy-goto-char-timer)
(define-key femacs-mode-map (kbd "o w") 'other-window)
(define-key femacs-mode-map (kbd "o i") 'clipboard-kill-ring-save)
(define-key femacs-mode-map (kbd "o q") 'kill-buffer-and-window)
(define-key femacs-mode-map (kbd "o o") 'keyboard-quit)

;;oo oi 取消选择 或esc。

;; (define-prefix-command 'femacs-i-prefix)
;; (define-key femacs-mode-map (kbd "i") 'femacs-i-prefix)
;; (define-key femacs-i-prefix (kbd "i") 'femacs-mark-whole-sexp)
;; (defun femacs-mark-whole-line ()
;;   "Select the current line."
;;   (interactive)
;;   (beginning-of-line)
;;   (set-mark (line-end-position)))
;; (define-key femacs-i-prefix (kbd "l") 'femacs-mark-whole-line)


;;mini-buffer
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




;;;;;;;;;;;;;;;;;;;;;;;pkg

(use-package projectile
  :ensure t
  :bind (("C-p" . projectile-command-map))
  :config
  (setq projectile-mode-line "P")
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

;; (use-package expreg
;;   :ensure t
;;   :bind (("C-a" . expreg-expand)
;; 	 ("C-e" . expreg-contract))
;;   :init
;;   ;; (setq expreg-functions
;;   ;;       '(expreg-expand-dwim     ;; 根据 context 自动扩展
;;   ;;         expreg-expand-using-tree-sitter
;;   ;;         expreg-expand-using-syntax))
;;   )

(use-package expand-region
  :ensure t
  :init
  ;; 添加额外的扩展规则
  (defun my/mark-comment ()
    "自定义规则：选中当前注释行或块。"
    (interactive)
    (when (nth 4 (syntax-ppss))
      (let ((bounds (bounds-of-thing-at-point 'comment)))
        (set-mark (car bounds))
        (goto-char (cdr bounds)))))
  (defun er/mark-line ()
  "选中整行（包含换行符）。"
  (interactive)
  (let ((beg (line-beginning-position))
        (end (min (point-max) (1+ (line-end-position)))))
    (set-mark beg)
    (goto-char end)
    ))
  (defun er/mark ()
  "选中整行（包含换行符）。"
  (interactive)
  (set-mark (point)))
  :config
  ;; 在 expand-region 的规则列表中插入自定义规则
  (setq expand-region-contract-fast-key "-"
        expand-region-reset-fast-key "0")
  ;(er/enable-mode-expansions 'prog-mode 'my/mark-comment)
					;(er/enable-mode-expansions 'text-mode 'er/mark-line)不要用，会自动选第一行
					;(er/enable-mode-expansions 'prog-mode 'er/mark-line)
  (add-to-list 'er/try-expand-list 'er/mark-line)
  (add-to-list 'er/try-expand-list 'er/mark)
  
  (defun er--collapse-region-before (&rest _)
  ;; FIXME: Re-use `er--first-invocation'?
;;  (when (memq last-command '(er/expand-region er/contract-region))
    (er/contract-region 0)))

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
;; To create a file, visit it with ‘<open>' and enter text in its buffer.

(define-key minibuffer-local-map (kbd "C-r") 'counsel-minibuffer-history)
(define-key ivy-minibuffer-map (kbd "C-p") 'ivy-previous-history-element)
(define-key ivy-minibuffer-map (kbd "C-j") 'ivy-next-line)
(define-key ivy-minibuffer-map (kbd "C-k") 'ivy-previous-line)
(define-key ivy-switch-buffer-map (kbd "C-k") 'ivy-previous-line)
(with-eval-after-load 'swiper
  (define-key swiper-map (kbd "C-l") 'ivy-done))

(define-key ivy-minibuffer-map (kbd "C-l") 'ivy-done)

;;;;;;;;;;;;;;;;;;func

(defun femacs-esc-to-femacs ()
  "Esc to femacsmode."
  (interactive)
  (if femacs-mode
      (call-interactively 'keyboard-escape-quit)
    (call-interactively 'femacs-mode)))


(defun femacs-RET ()
  "."
  (interactive)
  (newline)
  (call-interactively 'femacs-mode))

(defun femacs-DEL ()
  "."
  (interactive)
  (if (femacs-use-region-p)
      (let ()
	(call-interactively 'backward-delete-char-untabify)
	(call-interactively 'femacs-mode)
	)
      (call-interactively 'femacs-mode)
      )
 )

(defun femacs-mark-whole-sexp ()
  "."
  (interactive)
  (let ((bound (bounds-of-thing-at-point 'sexp)))
    (if bound
        (progn
          (goto-char (car bound))
          (set-mark (point))
          (goto-char (cdr bound)))
      (message "No sexp found at point!"))))

(defun femacs-expand-region ()
  "Expand region progressively: word → sexp → sentence → page.
Each time you call, the region will grow based on thing-at-point boundaries."
  (interactive)
  ;; 初次调用：设置 mark
  (catch 'done
    (unless (femacs-use-region-p)
      (set-mark-command nil)
      (message "Set mark.")
      (throw 'done nil))

    (let ((start (region-beginning))
          (end (region-end)))

      (dolist (thing '(word symbol number filename url email uuid sexp line list defun sentence))
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
      ;; 当前为 page
      (let ((page (bounds-of-thing-at-point 'page)))
        (when (and page
                  (= start (car page))
                  (= end (cdr page)))
	      (keyboard-escape-quit)
              (message "unSet mark.")
	      (throw 'done nil)))))
)

(defun femacs-use-region-p ()
  "."
  (and (mark) (region-active-p)))

(defun femacs-scroll-down-half-page-keep-cursor ()
  "Scroll down half a page while keeping point's relative position in the window."
  (interactive)
  (let* ((current-line (count-screen-lines (window-start) (point)))
         (half-page (max 1 (/ (window-body-height) 2))))
    (scroll-down-command half-page)
    (move-to-window-line current-line)))


(defun femacs-scroll-up-half-page-keep-cursor ()
  "Scroll up half a page while keeping point's relative position in the window."
  (interactive)
  (let* ((current-line (count-screen-lines (window-start) (point)))
         (half-page (max 1 (/ (window-body-height) 2))))
    (scroll-up-command half-page)
    (move-to-window-line current-line)))


(defun femacs-forward-select (move-fn)
  "Perform MOVE-FN with proper region expansion handling."
  (if (use-region-p)
      (let ((point-is-after-mark (< (point) (mark))))
        (if point-is-after-mark
            (exchange-point-and-mark))) ;; make point before mark
    )
  (funcall move-fn))
(defun femacs-backward-select (move-fn)
  "Perform MOVE-FN with proper region expansion handling."
  (if (use-region-p)
      (let ((point-is-before-mark (> (point) (mark))))
        (if point-is-before-mark
            (exchange-point-and-mark))) ;; make point before mark
    )
  (funcall move-fn))

(defun femacs-forward-word ()
  "."
  (interactive)
       (femacs-forward-select #'my/forward-by-type))

(defun femacs-backward-word ()
  "."
  (interactive)
  (femacs-backward-select #'my/backward-by-type))

(defun femacs-move-to-previous-bol ()
  "Move cursor to the beginning of the previous line."
  (interactive)
  (forward-char -1)
  (beginning-of-line))

(defun femacs-move-to-next-eol ()
  "Move cursor to the end of the next line."
  (interactive)
  (forward-char 1)
  (end-of-line))

(defun femacs-next-line ()
  "."
  (interactive)
  (femacs-forward-select #'femacs-move-to-next-eol))

(defun femacs-previous-line ()
  "."
  (interactive)
 (femacs-backward-select #'femacs-move-to-previous-bol))




(defun my/char-type (char)
  "Return the type of CHAR:
'space, 'word, 'bracket, 'newline, or 'symbol."
  (cond
   ((member char '(?\s ?\t)) 'space)
   ((char-equal char ?\n) 'newline)
   ((string-match-p "[[:alnum:]]" (char-to-string char)) 'word)
   ((string-match-p "[()\\[\\]{}<>]" (char-to-string char)) 'bracket)
   (t 'symbol)))
(defun my/skip-forward-by-type (type)
  "Skip forward while characters are of TYPE. Return t if more than 1 character skipped and not all space."
  (let ((start (point))
        (space-type (eq type 'space)))
    (while (and (not (eobp))
                (eq (my/char-type (char-after)) type))
      (forward-char))
    (let ((len (- (point) start)))
      (and (> len 1)
           (or (not space-type)
               (save-excursion
                 (goto-char start)
                 (not (string-match-p "\\`[ \t]+\\'" (buffer-substring start (point))))))))))
       (defun my/forward-by-type ()
  "Move forward to the end of next significant same-type character group."
  (interactive)
  (let ((type (my/char-type (char-after))))
    (when type
      (if (my/skip-forward-by-type type)
	  ()
          (my/skip-forward-by-type (my/char-type (char-after)))))))
(defun my/skip-backward-by-type (type)
  "Skip backward while characters are of TYPE. Return t if more than 1 character skipped and not all space."
  (let ((end (point))
        (space-type (eq type 'space)))
    (while (and (not (bobp))
                (eq (my/char-type (char-before)) type))
      (backward-char))
    (let ((len (- end (point))))
      (and (> len 1)
           (or (not space-type)
               (save-excursion
                 (let ((text (buffer-substring (point) end)))
                   (not (string-match-p "\\`[ \t]+\\'" text)))))))))

(defun my/backward-by-type ()
  "Move backward to the start of previous significant same-type character group."
  (interactive)
  (let ((type (my/char-type (char-before))))
    (when type
      (if (my/skip-backward-by-type type)
	  ()
          (my/skip-backward-by-type (my/char-type (char-before)))))))



(put 'scroll-left 'disabled nil)
