#! /usr/bin/env python
# -*- coding: utf-8 -*-

from constant import DEFAULT_FONT, DEFAULT_FONT_SIZE
from color import color_hex_to_cairo 
import cairo
import pango
import pangocairo




def draw_pixbuf(cr, pixbuf, x, y, alpha=1.0):
    cr.set_source_pixbuf(pixbuf, x, y)
    cr.paint_with_alpha(1.0)

def draw_text(cr, text, x, y, 
              text_size=DEFAULT_FONT_SIZE,
              text_color="#FFFFFF",
              text_font=DEFAULT_FONT,
              alignment=pango.ALIGN_LEFT,
              pango_list=None):
    cr.set_source_rgb(*color_hex_to_cairo(text_color)) 

    context = pangocairo.CairoContext(cr)
    layout = context.create_layout()
    layout.set_font_description(pango.FontDescription("%s %s" % (text_font, text_size)))
    layout.set_text(text) 
    # add pango list attributes.
    if pango_list:
        layout.set_attributes(pango_list)
    cr.move_to(x, y)
    context.update_layout(layout)
    context.show_layout(layout)

def draw_tray_text(cr, text, x, y, 
                  out_text_color="#000000",
                  in_text_color="#FFFFFF",
                  line_width=3,
                  text_font=DEFAULT_FONT,
                  text_size=DEFAULT_FONT_SIZE,
                  ):
    line_width = line_width
    cr_alpha = 0.5
    # set out text color.
    r, g, b = color_hex_to_cairo(out_text_color)
    context = pangocairo.CairoContext(cr)
    layout = context.create_layout()
    layout.set_font_description(pango.FontDescription("%s %s" % (text_font, text_size)))
    # set text.
    layout.set_text(text)
    #
    cr.move_to(x, y)
    cr.save()       
    cr.layout_path(layout)
    cr.set_line_width(line_width)
    cr.set_source_rgba(r, g, b, cr_alpha)
    cr.stroke_preserve()
    cr.fill()
    cr.restore()

    cr.save()
    cr.new_path()

    r, g, b = color_hex_to_cairo(in_text_color) 
    cr.set_source_rgb(r, g, b)
    cr.set_operator(cairo.OPERATOR_OVER)

    cr.move_to(x, y)       
    context.show_layout(layout)
        
