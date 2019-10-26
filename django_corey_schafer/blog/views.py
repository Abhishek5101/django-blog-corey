from django.shortcuts import render

posts = [
	{
		'author': 'Abhi',
		'title': 'Blog post',
		'content': 'Abhi\'s post',
		'date': 'Oct 26 2019'
	},
	{
		'author': 'John Doe',
		'title': 'John\'s post',
		'content': 'john\'s content',
		'date': 'Oct 26 2019'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html')
