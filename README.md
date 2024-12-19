For setup docker-hub push 
add this code to youre pipeline (.gitlab-ci.yml)


```yaml
docker-hub-push:
  stage: push
  script:
    - echo "Logging into Docker Hub..."
    - echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
    - echo "Tagging Docker Image..."
    - docker tag $DOCKER_IMAGE $DOCKER_USERNAME/fastapi-app:latest
    - echo "Pushing Docker Image to Docker Hub..."
    - docker push $DOCKER_USERNAME/fastapi-app:latest
  only:
    - main
