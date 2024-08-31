# ui components
The ui components use css for styling, you can find the different styles in the main css file, 
here is the full path:
```
static/css/main.css
```


## Buttons
There are 6 different button variants: **primary, secondary, outline, destructive, ghost, link**.\
You can change the Button variant by giving the button a *variant* attribute.
```html
<button variant="primary">Primary</button>
```
The default variant is the *primary* variant, so if you didn't provide a variant attribute, the variant will be *primary*.
```html
<button>Primary</button>
```
The buttons can also be disabled by passing the **disabled** attribute to them
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
{% from "/components/ui/animated_icons.html" import Loading %}

<button variant="primary" disabled>
  {{ Loading(fill='var(--primary-foreground)') }}
  Loading
</button>
```


## DropDownMenu

Unlike other ui components, the *DropDownMenu* uses a custome css and js files.\
here is the path of the DropDownMenu components:
```
templates/components/ui/dropdown_menu.html
```
and this is path of it's css file:
```
static/css/components/ui/dropdown_menu.html
```
and this is path of it's js file:
```
static/js/components/ui/dropdown_menu.html
```

### DropDownMenu js code
The DropDownMenu js code contains 3 functions:
```js
// for the DropDownMenu trigger
dropDownClickShowHide(event)

// for closing all the DropDownMenus
closeAllDropDowns()

// this is used in the windowEvents.js file
handleWindowClickForDropDown(event)
```
### Using the DropDownMenu
The DropDownMenu can be used by importing it with:
```html
{% from "/components/ui/dropdown_menu.html" import DropdownMenu %}
```

The DropDownMenu takes 5 arguments: **class** for the DropDownMenu class, **contentClass** for the DropDownMenu content class, **triggerText** for the trigger button, **triggerVariant** for the trigger button variant the default is the *outline* variant, **triggerClass** for the trigger button class.\
Example code:
```html
{% call DropDownMenu(triggerText='Open') %}
  <a href="#Link1">Link1</a>
  <a href="#Link2">Link2</a>
  <a href="#Link3">Link3</a>
{% endcall %}
```

Clicking on any DropDownMenu child element will cause it to close, so does clicking on any other part of the application.\
If you do not want an element to close the DropDownMenu you can add **dropDownPreventClose** attribute to it.\
Example code:
```html
{% call DropDownMenu() %}
  <div dropDownPreventClose >this is a description</div>
  <button>Close</button>
{% endcall %}
```
DropDownMenu children accepts a class name called **ui-dropdown-menu-item**, this will style them with some custom style.\
Example code:
```html
{% call DropDownMenu() %}
  <div calss="ui-dropdown-menu-item">Item</div>
{% endcall %}
```

## Separator
There are two types of separators, both use the `<hr/>` tag.\
You can set the orientation, by giving it an **orientation** attribute which would be either *horizontal* or *vertical*.\
The deafult is *horizontal*, so `<hr/>` without any attributes would be horizontal.\
Example code:
```html
<hr orientation="vertical" />
```

## Links
Links are simple just use the a tag, if the link is selected then add the **active** tag to it
Example code:

```html
<a active >Link_1</a>
<a >Link_2</a>
```




