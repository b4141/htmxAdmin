# ui components
The ui components use css for styling, you can find the different styles in the main css file, 
here is the full path:
```
static/css/main.css
```


## Buttons
There are 6 different button variants: *primary, secondary, outline, destructive, ghost, link*.\
You can change the Button variant by giving the button a *variant* attribute.
```html
<button variant="primary">Primary</button>
```
The default variant is the *primary* variant, so if you didn't provide a variant attribute, the variant will be *primary*.
```html
<button>Primary</button>
```
The buttons can also be disabled by passing the *disabled* attribute to them
```html
<button disabled>Primary Disabled</button>
```


### Button Variants
**Primary Button**
```html
<button variant="primary">Primary</button>
```

**Secondary Button**
```html
<button variant="secondary">Secondary</button>
```

**Secondary Button**
```html
<button variant="secondary">Secondary</button>
```

**Outline Button**
```html
<button variant="outline">Outline</button>
```

**Destructive Button**
```html
<button variant="destructive">Destructive</button>
```

**Ghost Button**
```html
<button variant="ghost">Ghost</button>
```

**Link Button**
```html
<button variant="link">Link</button>
```

**Other Button Types**\
You can also add *icons* to the button, this is an example of a loading state:
```html
<button variant="primary" disabled>
  {{ Loading(fill='var(--primary-foreground)') }}
  Loading
</button>
```
