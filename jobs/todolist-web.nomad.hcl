job "todolist-web" {
  type = "service"

  group "td-web" {
    count = 1
    network {
      port "django" {
        static = 8000
      }
    }

    service {
      name     = "todolist-svc"
      port     = "django"
      provider = "nomad"
    }

    task "todolist-task" {
      driver = "docker"

      config {
        image = "todolist-web:local"
        ports = ["django"]
      }
    }
  }
}
