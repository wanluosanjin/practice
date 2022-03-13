(add-to-list
 'load-path
 (expand-file-name "myel" user-emacs-directory))

;(eval '(+ 1 1))

;;eval((require (quote myel)) nil)
(require 'myel)
;;(autoload 'copy-to-next-line "myel" t t)
;;(autoload 'exchange-next-line "myel" t t)
(provide 'init)
