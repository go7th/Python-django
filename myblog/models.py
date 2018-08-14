from django.db import models

# Create your models here.
# class Article(models.Model):
#     title=models.CharField(max_length=32,default="title")
#     content = models.TextField(null=True)
        

# from django.db import models
 
 
# class Menu(models.Model):
#     #  '''页面中的菜单名'''
#      title = models.CharField(max_length=32)
 
# class Group(models.Model):
#     # '''权限url所属的组'''
#     caption = models.CharField(verbose_name='组名称',max_length=32)
#     menu =models.ForeignKey(verbose_name='组所属菜单',to='Menu',default=1)  # 组所在的菜单

#     class Meta:
#         verbose_name_plural = 'Group组表'

#     def __str__(self):
#         return self.caption

# class User(models.Model):
#     # """
#     # 用户表
#     # """
#     username = models.CharField(verbose_name='用户名',max_length=32)
#     password = models.CharField(verbose_name='密码',max_length=64)
#     email = models.CharField(verbose_name='邮箱',max_length=32)

#     roles = models.ManyToManyField(verbose_name='具有的所有角色',to="Role",blank=True)
#     class Meta:
#         verbose_name_plural = "用户表"

#     def __str__(self):
#         return self.username

# class Role(models.Model):
#     # """
#     # 角色表
#     # """
#     title = models.CharField(max_length=32)
#     permissions = models.ManyToManyField(verbose_name='具有的所有权限',to='Permission',blank=True)
#     class Meta:
#         verbose_name_plural = "角色表"

#     def __str__(self):
#         return self.title


# class Permission(models.Model):
#     # """
#     # 权限表
#     # """
#     title = models.CharField(verbose_name='标题',max_length=32)
#     url = models.CharField(verbose_name="含正则URL",max_length=64)
#     is_menu = models.BooleanField(verbose_name="是否是菜单")

#     code = models.CharField(verbose_name='url代码',max_length=32,default=0)  # 路径对应的描述名称
#     group = models.ForeignKey(verbose_name='所属组',to='Group',null=True,blank=True)    # 所属组

#     class Meta:
#         verbose_name_plural = "权限表"

#     def __str__(self):
#         return self.titlemodel


class UserType(models.Model):
    caption = models.CharField(max_length=32)
    pass
# class UserInfo(models.Model):
#     username = models.CharField(max_length=32)
#     age = models.IntegerField()
#     user_type = models.ForeignKey('UserType')