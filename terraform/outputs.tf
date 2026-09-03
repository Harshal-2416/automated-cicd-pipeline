output "server_public_ip" { 
  value = aws_instance.app_server.public_ip 
} 
output "ecr_repository_url" { 
  value = aws_ecr_repository.app.repository_url 
} 
output "vpc_id" { 
  value = aws_vpc.main.id 
} 
