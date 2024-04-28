job "todolist-celery" {
  type = "service"

  group "td-celery" {
    count = 1
    network {
      port "celery" {
        static = 8000
      }
    }

    service {
      name     = "todolist-worker-svc"
      port     = "celery"
      provider = "nomad"
    }

    task "todolist-task" {
      driver = "docker"

      config {
        image = "todolist-celery:local"
        ports = ["celery"]
      }
    }
  }
}
