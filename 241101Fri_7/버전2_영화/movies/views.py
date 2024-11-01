from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
import requests

from django.conf import settings


from .models import Actor, Movie, Review
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer, CreateReviewSerializer
from django.views.decorators.csrf import csrf_exempt
import json

# 전체 배우 목록 제공
@require_http_methods(["GET"])
def actor_list(request):
    actors = Actor.objects.all().values("id", "name")
    return JsonResponse(list(actors), safe=False)


# 단일 배우 정보 제공 (출연 영화 제목 포함)
@require_http_methods(["GET"])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, id=actor_pk)
    movies = actor.movies.all().values("title")
    data = {
        "id": actor.pk,
        "name": actor.name,
        "movies": list(movies),
    }
    return JsonResponse(data)


# 전체 영화 목록 제공
@require_http_methods(["GET"])
def movie_list(request):
    movies = Movie.objects.all().values("title", "overview")
    # movies = Movie.objects.all().values("id", "title", "overview", "release_date", "poster_path")
    return JsonResponse(list(movies), safe=False)


# 단일 영화 정보 제공 (출연 배우 이름과 리뷰 목록 포함)
@require_http_methods(["GET"])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    actors = movie.actors.all().values("name")
    reviews = movie.reviews.all().values("title", "content")
    data = {
        "id": movie.pk,
        "actors": list(actors),  # 배우 목록
        "reviews": list(reviews),  # 리뷰 목록
        "title": movie.title,
        "overview": movie.overview,
        "release_date": movie.release_date.isoformat(),
        "poster_path": movie.poster_path,
    }
    return JsonResponse(data)


# 전체 리뷰 목록 제공
@require_http_methods(["GET"])
def review_list(request):
    reviews = Review.objects.all().values("title", "content")
    return JsonResponse(list(reviews), safe=False)


# 단일 리뷰 조회, 수정, 삭제 (출연 영화 제목 포함)
@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, id=review_pk)

    if request.method == "GET":
        data = {
            "id": review.pk,
            "movie_title": review.movie.title,
            "title": review.title,
            "content": review.content,
        }
        return JsonResponse(data)

    elif request.method == "PUT":
        # print(request.body)
        # data = json.loads(request.body)
        data = json.loads(request.body.decode('utf-8'))
        review.title = data.get("title", review.title)
        review.content = data.get("content", review.content)
        review.save()
        return JsonResponse({
            "id": review.pk,
            "movie_title": review.movie.title,
            "title": review.title,
            "content": review.content,
        })
    

    elif request.method == "DELETE":
        review.delete()
        return JsonResponse({"message": "review 1 is deleted"}, status=204)


# 리뷰 생성
@api_view(['POST'])
def create_review(request):
    serializer = CreateReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# @csrf_exempt
# @require_http_methods(["POST"])
# def create_review(request):
#     data = json.loads(request.body)
#     movie_pk = data.get("movie_pk")
#     movie = get_object_or_404(Movie, id=movie_pk)
#     review = Review.objects.create(
#         movie=movie,
#         title=data.get("title"),
#         content=data.get("content")
#     )
#     return JsonResponse({
#         "id": review.pk,
#         "movie_title": movie.title,
#         "title": review.title,
#         "content": review.content,
#     }, status=201)


# @require_http_methods(["POST"])
# def create_review(request):
#     try:
#         data = json.loads(request.body)
#     except json.JSONDecodeError:
#         return JsonResponse({"error": "유효하지 않은 JSON입니다."}, status=400)

#     movie_pk = data.get("movie_pk")
#     title = data.get("title")
#     content = data.get("content")

#     if not movie_pk or not title or not content:
#         return JsonResponse({"error": "필수 필드가 누락되었습니다."}, status=400)

#     movie = get_object_or_404(Movie, id=movie_pk)

#     review = Review.objects.create(
#         movie=movie,
#         title=title,
#         content=content
#     )

#     return JsonResponse({
#         "id": review.pk,
#         "movie_title": movie.title,
#         "title": review.title,
#         "content": review.content,
#     }, status=201)