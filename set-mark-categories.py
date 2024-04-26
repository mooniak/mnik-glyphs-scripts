# MenuTitle: Fix Sinhala mark categories
# -*- coding: utf-8 -*-

def set_category_and_subcategory(glyphs_list):
    for glyph_name in glyphs_list:
        glyph = Glyphs.font.glyphs[glyph_name]
        
        if glyph:
            glyph.category = "Mark"
            glyph.subCategory = "Spacing"
            print(f"Set category and subcategory for {glyph_name}")
        else:
            print(f"Glyph {glyph_name} not found in the font")

# Example usage:
glyphs_list = [
"0D82",
"0DD3",
"0DDC",
"0DD6",
"0DDE",
"0D83",
"0DD4",
"0DDD",
"0DCF",
"0DD1",
"0DD8",
"0DDA",
"0DF3",
"0DCA",
"0DD0",
"0DD2",
"0DD9",
"0DDB",
"0DF2",
"0DF4",
"0DDF",

]  # Replace with your actual list of glyph names
set_category_and_subcategory(glyphs_list)


