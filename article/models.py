from django.db import models
from uuid import uuid4
# Create your models here.


class Article(models.Model):
    ARTICLE_STATUS = (
        ('0', '正常'),
        ('1', '删除')
    )

    # 编号
    id = models.UUIDField(verbose_name="文章编号", default=uuid4, primary_key=True)
    # 标题
    title = models.CharField(verbose_name='文章标题', max_length=200)
    # 内容
    content = models.TextField(verbose_name='内容')
    # 发布时间
    pub_time = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)
    # 阅读次数
    read_count = models.IntegerField(verbose_name='阅读次数', default=0)
    # 点赞次数
    admired_count = models.IntegerField(verbose_name="点赞次数", default=0)
    # 喜欢次数
    like_count = models.IntegerField(verbose_name="喜欢次数", default=0)
    # 收藏次数
    collected_count = models.IntegerField(verbose_name="收藏次数", default=0)
    # 评论次数
    comment_count = models.IntegerField(verbose_name="评论次数", default=0)
    # 修改时间
    update_time = models.DateTimeField(verbose_name="上次修改时间", auto_now=True)
    # 状态
    status = models.CharField(verbose_name='上次修改时间', choices=ARTICLE_STATUS, max_length=4)
    # 文章作者，外键约束
    article_author = models.ForeignKey('author.Author', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-pub_time', 'id']

    def __str__(self):
        return f"文章标题{self.title}，文章内容{self.content}"