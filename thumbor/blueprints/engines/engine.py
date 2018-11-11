#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com
"""
Thumbor engine. This class triggers events that should be implemented by each engine.

All methods are static coroutines.
"""

from tornado import gen

from thumbor.lifecycle import Events


class Engine(object):
    "Engine class. Triggers events captured by the engine blueprints."

    @classmethod
    async def read_image(cls, sender, details, buffer):
        """
        Triggers the read image event.
        """
        await Events.trigger(
            Events.Engine.before_read_image, sender, details=details, buffer=buffer
        )

        await Events.trigger(
            Events.Engine.read_image, sender, details=details, buffer=buffer
        )

        await Events.trigger(
            Events.Engine.after_read_image, sender, details=details, buffer=buffer
        )

    @classmethod
    async def resize(cls, sender, details, width=0, height=0):
        """
        Triggers the resize engine event.
        """
        await Events.trigger(
            Events.Engine.before_resize,
            sender,
            details=details,
            width=width,
            height=height,
        )

        await Events.trigger(
            Events.Engine.resize, sender, details=details, width=width, height=height
        )

        await Events.trigger(
            Events.Engine.after_resize,
            sender,
            details=details,
            width=width,
            height=height,
        )

    @classmethod
    async def crop(
        cls, sender, details, left, top, right, bottom
    ):  # pylint: disable=too-many-arguments
        """
        Triggers the crop engine event.
        """
        await Events.trigger(
            Events.Engine.before_crop,
            sender,
            details=details,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        await Events.trigger(
            Events.Engine.crop,
            sender,
            details=details,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        await Events.trigger(
            Events.Engine.after_crop,
            sender,
            details=details,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

    @classmethod
    async def flip_horizontally(cls, sender, details):
        """Triggers the flip horizontally engine event."""
        await Events.trigger(
            Events.Engine.before_flip_horizontally, sender, details=details
        )

        await Events.trigger(Events.Engine.flip_horizontally, sender, details=details)

        await Events.trigger(
            Events.Engine.after_flip_horizontally, sender, details=details
        )

    @classmethod
    async def flip_vertically(cls, sender, details):
        """Triggers the flip vertically engine event."""
        await Events.trigger(
            Events.Engine.before_flip_vertically, sender, details=details
        )

        await Events.trigger(Events.Engine.flip_vertically, sender, details=details)

        await Events.trigger(
            Events.Engine.after_flip_vertically, sender, details=details
        )

    @classmethod
    async def reorientate(cls, sender, details):
        "Reorientates the image according to metadata"
        await Events.trigger(Events.Engine.before_reorientate, sender, details=details)

        await Events.trigger(Events.Engine.reorientate, sender, details=details)

        await Events.trigger(Events.Engine.after_reorientate, sender, details=details)

    @classmethod
    async def get_image_data_as_rgb(cls, sender, details):
        "Get Image data as RGB Buffer"
        image_mode, image_data = await Events.trigger(
            Events.Engine.get_image_data_as_rgb, sender, details=details
        )

        return image_mode.encode("utf-8"), image_data

    @classmethod
    async def set_image_data(cls, sender, details, data):
        "Sets image data into the engine using buffer"
        await Events.trigger(
            Events.Engine.set_image_data, sender, details=details, data=data
        )

    @classmethod
    async def get_image_size(cls, sender, details):
        "Get Image size"
        image_size = await Events.trigger(
            Events.Engine.get_image_size, sender, details=details
        )

        return image_size

    @classmethod
    async def serialize(cls, sender, details):
        """
        Triggers the serialize image event.
        """
        await Events.trigger(Events.Engine.before_serialize, sender, details=details)

        await Events.trigger(Events.Engine.serialize, sender, details=details)

        await Events.trigger(Events.Engine.after_serialize, sender, details=details)

    @classmethod
    async def get_proportional_width(cls, sender, details, new_height):
        width, height = await cls.get_image_size(sender, details)

        return round(float(new_height) * width / height, 0)

    @classmethod
    async def get_proportional_height(cls, sender, details, new_width):
        width, height = await cls.get_image_size(sender, details)

        return round(float(new_width) * height / width, 0)

    @classmethod
    async def focus(cls, sender, details):
        await Events.trigger(
            Events.Engine.before_focal_points_changed,
            sender,
            details=details,
            focal_points=details.focal_points,
        )

        await Events.trigger(
            Events.Engine.focal_points_changed,
            sender,
            details=details,
            focal_points=details.focal_points,
        )

        await Events.trigger(
            Events.Engine.after_focal_points_changed,
            sender,
            details=details,
            focal_points=details.focal_points,
        )

    @classmethod
    async def draw_rectangle(cls, sender, details, left, top, width, height):
        await Events.trigger(
            Events.Engine.draw_rectangle,
            sender,
            details=details,
            left=left,
            top=top,
            width=width,
            height=height,
        )

    @classmethod
    async def convert_to_grayscale(
        cls, sender, details, update_image=False, with_alpha=False
    ):
        img = await Events.trigger(
            Events.Engine.convert_to_grayscale,
            sender,
            details=details,
            update_image=update_image,
            with_alpha=with_alpha,
        )

        return img