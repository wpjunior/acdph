#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import Image
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from settings import MEDIA_ROOT
from os.path import splitext
from hashlib import md5
from django.core.files.base import ContentFile

THUMBNAIL = (150, 150)
THUMB = (300, 300)
VIEW = (600, 400)


class BasePhoto(models.Model):
    name = models.CharField("Nome", max_length=100)
    image = models.ImageField("Foto", upload_to='photo',
                              height_field="heigth", width_field="width")

    width = models.IntegerField(default=0)
    heigth = models.IntegerField(default=0)

    class Meta:
        db_table = "django_basephoto"

    def __unicode__(self):
        return self.name
"""
    

    def get_photo_thumb(self):

        def get_photo_thumb_filename():
            file, ext = os.path.splitext(self.image.path)
            return file + '_%sx%s' % THUMB + ext

        def get_photo_thumb_url():
            url, ext = os.path.splitext(self.image.url)
            return url + '_%sx%s' % THUMB + ext

        thumb = get_photo_thumb_filename()

        if not os.path.exists(thumb):
            img = Image.open(self.image.path)
            img.thumbnail(THUMB, Image.ANTIALIAS)
            img.save(thumb)

        return get_photo_thumb_url()

    def get_photo_view(self):

        def get_photo_view_filename():
            file, ext = os.path.splitext(self.image.path)
            return file + '_%sx%s' % VIEW + ext

        def get_photo_view_url():
            url, ext = os.path.splitext(self.image.url)
            return url + '_%sx%s' % VIEW + ext

        thumb = get_photo_view_filename()

        if not os.path.exists(thumb):
            img = Image.open(self.image.path)
            img.thumbnail(VIEW, Image.ANTIALIAS)
            img.save(thumb)

        return get_photo_view_url()

    def delete_files(self):

        if os.path.isfile(self.image.path):
            os.remove(self.image.path)

        f, ext = os.path.splitext(self.image.path)
        d = f + '_%sx%s' % THUMBNAIL + ext

        if os.path.isfile(d):
            os.remove(d)

        d = f + '_%sx%s' % THUMB + ext

        if os.path.isfile(d):
            os.remove(d)

        d = f + '_%sx%s' % VIEW + ext

        if os.path.isfile(d):
            os.remove(d)
"""

class Photo(BasePhoto):
    content_type = models.ForeignKey(ContentType, related_name="photo_content_type")
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    thumbnail = models.ForeignKey(BasePhoto, blank=True, null=True,
                                  related_name="thumbnail")

    view = models.ForeignKey(BasePhoto, blank=True, null=True,
                             related_name="view")

    class Meta:
        db_table = "django_photo"

    def get_photo_thumbnail(self):
        print self.thumbnail
        print self.thumbnail
        if ((not self.thumbnail) or (not os.path.exists(self.thumbnail.path))):
            img = Image.open(self.image.path)
            img.thumbnail(THUMBNAIL, Image.ANTIALIAS)
            contents = img.tostring()
            hash = md5(contents).hexdigest()
            b, ext = splitext(self.image.path)
            filename = "%s%s" % (hash, ext)

            thumbnail = BasePhoto()
            thumbnail.image.save(filename, ContentFile(contents))
            thumbnail.save()
            print thumbnail
            self.thumbnail = thumbnail
            self.save()

        return self.thumbnail.url

class Album(models.Model):
    name = models.CharField("Nome", max_length=100)
    local = models.CharField("Local", max_length=150)
    desc = models.TextField("Descrição")
    date = models.DateField("Data")

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albuns"
        db_table = "django_album"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/albuns/%d/" % self.id

    def get_all_photos(self):
        album_type = ContentType.objects.get_for_model(self)
        all = Photo.objects.filter(content_type__pk=album_type.id,
                                   object_id=self.id)
        return all

"""
    def get_first_foto_thumbnail(self):
        a = Foto.objects.filter(content_object=self)
        if a:
            return a[0].get_photo_thumbnail()

    def get_first_foto_thumb(self):
        a = Photo.objects.filter(content_object=self)
        if a:
            return a[0].get_photo_thumb()

    def delete(self, *args, **kwargs):
        for foto in Photo.objects.filter(content_object=self):
            foto.delete_files()
            foto.delete()

        super(Imovel, self).delete(*args, **kwargs)
"""
    
