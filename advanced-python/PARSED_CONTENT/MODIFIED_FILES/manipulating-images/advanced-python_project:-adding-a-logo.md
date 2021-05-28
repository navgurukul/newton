```ngMeta
project:-adding-a-logo_key1
```
# project:-adding-a-logo_key2
project:-adding-a-logo_key3

project:-adding-a-logo_key4

project:-adding-a-logo_key5

project:-adding-a-logo_key6

project:-adding-a-logo_key7

project:-adding-a-logo_key8

project:-adding-a-logo_key9

project:-adding-a-logo_key10

project:-adding-a-logo_key11

project:-adding-a-logo_key12

project:-adding-a-logo_key13

project:-adding-a-logo_key14

project:-adding-a-logo_key15

project:-adding-a-logo_key16

project:-adding-a-logo_key17

project:-adding-a-logo_key18

project:-adding-a-logo_key19

project:-adding-a-logo_key20

# project:-adding-a-logo_key21
project:-adding-a-logo_key22


project:-adding-a-logo_key23 project:-adding-a-logo_key24
 project:-adding-a-logo_key25
project:-adding-a-logo_key26

project:-adding-a-logo_key27

project:-adding-a-logo_key28

 project:-adding-a-logo_key29
 project:-adding-a-logo_key30
 project:-adding-a-logo_key31
 project:-adding-a-logo_key32
 project:-adding-a-logo_key33
 project:-adding-a-logo_key34
project:-adding-a-logo_key35

project:-adding-a-logo_key36

project:-adding-a-logo_key37

# project:-adding-a-logo_key38
project:-adding-a-logo_key39


project:-adding-a-logo_key40 project:-adding-a-logo_key41
 project:-adding-a-logo_key42
project:-adding-a-logo_key43

project:-adding-a-logo_key44

project:-adding-a-logo_key45```python
   # Loop over all files in the working directory.
❶ for filename in os.listdir('.'):
❷     if not (filename.endswith('.png') or filename.endswith('.jpg')) \
          or filename == LOGO_FILENAME:
❸         continue # skip non-image files and the logo file itself

❹     im = Image.open(filename)
       width, height = im.size
```
project:-adding-a-logo_key46

# project:-adding-a-logo_key47
project:-adding-a-logo_key48


project:-adding-a-logo_key49 project:-adding-a-logo_key50
 project:-adding-a-logo_key51
project:-adding-a-logo_key52

project:-adding-a-logo_key53```python
      # Check if image needs to be resized.
      if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
          # Calculate the new width and height to resize to.
          if width > height:
❶            height = int((SQUARE_FIT_SIZE / width) * height)
              width = SQUARE_FIT_SIZE
          else:
❷            width = int((SQUARE_FIT_SIZE / height) * width)
              height = SQUARE_FIT_SIZE

          # Resize the image.
          print('Resizing %s...' % (filename))
     ❸     im = im.resize((width, height))
```
project:-adding-a-logo_key54

project:-adding-a-logo_key55

project:-adding-a-logo_key56

# project:-adding-a-logo_key57
project:-adding-a-logo_key58

project:-adding-a-logo_key59

project:-adding-a-logo_key60


project:-adding-a-logo_key61 project:-adding-a-logo_key62
 project:-adding-a-logo_key63
project:-adding-a-logo_key64

project:-adding-a-logo_key65

```python
    # Add the logo.
❶  print('Adding logo to %s...' % (filename))
❷  im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
❸  im.save(os.path.join('withLogo', filename))
```
project:-adding-a-logo_key66


project:-adding-a-logo_key67

# project:-adding-a-logo_key68
project:-adding-a-logo_key69

project:-adding-a-logo_key70

project:-adding-a-logo_key71

project:-adding-a-logo_key72

project:-adding-a-logo_key73

