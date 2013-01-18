(ql:quickload :mcclim)

(use-package :clim-user)

(in-package :clim-user)

(define-application-frame hello-world ()
  ((greeting :initform "Hey world"
             :accessor greeting))
  (:pane (make-pane 'hello-world-pane)))

(defclass hello-world-pane
    (clim-stream-pane) ())

(run-frame-top-level
 (make-application-frame 'hello-world))
