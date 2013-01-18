(ql:quickload :ltk)
(use-package :ltk)

;;;; read data

;; get colors for file extensions

;;;; utility functions

(defun concat (&rest strings)
  (format nil "~{~A~}" strings))

(defun main-interface ()
  (with-ltk ()
    (let* ((root (make-instance 'frame))
           (input (make-instance 'text
                                :master root
                                :background "#000000"
                                :foreground "#ffffff"
                                :takefocus t
                                :height 1))
           (canv (make-instance 'canvas
                                :master root
                                :background "#000000")))
      (pack root :fill :both :expand t)
      (pack input :fill :x :side :bottom)
      (pack canv :fill :both :expand t :side :top))))

(defun hidden-filep (pathname)
  (let ((name (or (pathname-name pathname)
                  (car (last (pathname-directory pathname))))))
    (equal "." (subseq name 0 1))))

;; (defun expand-pathname (pathname)
;;   (

(defun directory-files (directory &optional (extension "*.*") (hiddenp nil)) ; apparently *.* lists files even WITHOUT dots in them. who would've guessed???
  "Returns a list of all files in the directory."
  (let* ((ext (if (equal extension "/") "*/" extension))
         (listing (directory (pathname (concat directory "/" ext)))))
    (if hiddenp
        listing
        (remove-if #'hidden-filep listing))))

(main-interface)
