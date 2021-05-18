from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from classroom.models import Course
from classroom.api.serializers import CourseSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

@api_view(['GET', ])
def api_detail_coruse_view(request, cid):
	Courses = Course()
	try:
		Courses = Course.objects.get(cid=str(cid))
	except Courses.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CourseSerializer(Courses)
		return Response(serializer.data)


# @api_view(['PUT',])
# def api_update_blog_view(request, slug):

# 	try:
# 		blog_post = BlogPost.objects.get(slug=slug)
# 	except BlogPost.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'PUT':
# 		serializer = BlogPostSerializer(blog_post, data=request.data)
# 		data = {}
# 		if serializer.is_valid():
# 			serializer.save()
# 			data[SUCCESS] = UPDATE_SUCCESS
# 			return Response(data=data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE',])
# def api_delete_blog_view(request, slug):

# 	try:
# 		blog_post = BlogPost.objects.get(slug=slug)
# 	except BlogPost.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'DELETE':
# 		operation = blog_post.delete()
# 		data = {}
# 		if operation:
# 			data[SUCCESS] = DELETE_SUCCESS
# 		return Response(data=data)


# @api_view(['POST'])
# def api_create_blog_view(request):

# 	account = Account.objects.get(pk=1)

# 	blog_post = BlogPost(author=account)

# 	if request.method == 'POST':
# 		serializer = BlogPostSerializer(blog_post, data=request.data)
# 		data = {}
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




