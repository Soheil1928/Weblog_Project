from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Comment
from .forms import AddPostForm, EditPostForm, AddCommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View


class HomeView(ListView):
    model = Post
    template_name = 'blog_app/home.html'
    context_object_name = 'posts'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        like_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_like = like_post.total_likes()
        liked = False
        if like_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        context['total_like'] = total_like
        return context


def like_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=str(pk)))


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'blog_app/add_post.html'
    # fields = '__all__'       .چون فیلد ها رو از فرم میگیره این قسمت دیگه نیاز نیست


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog_app/edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog_app/delete_post.html'
    success_url = reverse_lazy('home')


class CategoryListView(ListView):
    model = Category
    template_name = 'blog_app/category_list.html'
    context_object_name = 'category_list'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog_app/add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('add_category')


def category(request, cat):
    category_post = Post.objects.filter(category=cat.replace('-', ' '))
    return render(request, 'blog_app/category.html', {'cat': cat.replace('-', ' '), 'category_post': category_post})
    


class AddCommentView(View):
    def get(self, request, pk):
        form = AddCommentForm()
        return render(request, 'blog_app/add_comment.html', {'form': form})
    
    def post(self, request, pk):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = Comment(name=form.cleaned_data.get('name'),
                              body=form.cleaned_data.get('body'),
                              post_id=pk)
            comment.save()

            return redirect('post_detail', pk=pk)
        return redirect('home')
