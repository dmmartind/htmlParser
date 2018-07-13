<?php





$lp->snippets = [
                     'listing_type' => $listing_type,
                     'product_id' => $product['itemcode'],
                     'altcode' => $product['altpartnumber'],
                     'name' => $product['desc4'],
                     'link' => $this->aTag([
                         'product_id' => $product['itemcode']
                     ], true),
                     'image' => [
                         'original' => WS_DIR_IMAGES . $product['filename_image'],
                         'thumbnail' => $image->imageThumbnail(FS_DIR_HTTP_ROOT . WS_DIR_IMAGES . $product['filename_image'], $width, $height, $this->category_image_clipping,$this->product_image_trim ),
                         'thumbnail_2x' => $image->imageThumbnail(FS_DIR_HTTP_ROOT . WS_DIR_IMAGES . $product['filename_image'], width*2, $height*2, $this->category_image_clipping, $this->product_image_trim),
                         'viewport' => [
                             'width' => $width,
                             'height' => $height,
                         ],
                     ],
                     'sticker' => $sticker,
                     'vendor' => $product['vendor_name'],
                     'short_description' => $product['desc1'],
                     'long_description' => $product['desc2'],
                     'unit' => $product['unit'],
                     'regular_price' => $tax->getPrice($product['list'], $product['tax_class_id']),
                     'discount_price' => (float)$product['discount_price'] ? $tax->getPrice($product['discount_price'],$product['tax_class_id']) : null,
                     'class_family' => $product['class_family'],
                     'class_group' => $product['class_group'],
                     'class_subheading' => $product['class_subheading'],
                     'class_category' => $product['class_category'],
                     'class_subcategory' => $product['class_subcategory'],
                     'weight' => $product['weight']
                 ];


?>

