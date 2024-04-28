job "todolist-redis" {
  type = "service"

  group "td-redis" {
    count = 1
    network {
      port "redis" {
        static = 6379
      }
    }

    service {
      name     = "redis-svc"
      port     = "redis"
      provider = "nomad"
    }

    task "redis-task" {
      driver = "docker"

      config {
        image = "redis:latest"
        ports = ["redis"]
      }
    }
  }
}
