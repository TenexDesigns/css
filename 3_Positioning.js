
*               ********** POSITIONS IN HTML  **********
  ---> Static
  ---> Relative
  ---> Absolute
  ---> Fixed
  ---> Sticky

STATIC---->This is the default position for HTML elements. Elements with a static position are positioned according to the normal flow of the document. They are not affected by the top, bottom, left, right, or z-index properties.
RELATIVE ----> Relative: Elements with a relative position are positioned relative to their normal position in the document flow. They can be moved using the top, bottom, left, and right properties. Other elements on the page are not affected by the movement of elements with a relative position.
ABSOLUTE----> Absolute: Elements with an absolute position are positioned relative to the nearest positioned ancestor (an ancestor with a position value other than static) or the initial containing block if no positioned ancestor is found. Absolute positioned elements are taken out of the normal flow of the document. They can be moved using the top, bottom, left, and right properties. Other elements on the page can overlap absolute positioned elements.
Fixed: Elements with a fixed position are positioned relative to the viewport (the browser window). They stay in the same position even when the page is scrolled. Fixed positioned elements are taken out of the normal flow of the document. They can be moved using the top, bottom, left, and right properties. Other elements on the page can overlap fixed positioned elements.
Sticky: Elements with a sticky position are positioned based on the users scroll position. They act like a hybrid between relative and fixed positions. Sticky positioned elements are positioned relative until a given offset position is met in the viewport, and then they "stick" in place, behaving like fixed positioned elements.

1. static: Default one.-Elements with static positioning are placed in the normal flow of the document.They are not affected by the top, bottom, left, or right properties.
2. relative : Same as static.But it removes the item with the relative posion form the floe/dom/html view in browser.
   But it lets you add top, right, bottom, left.Adding relative does not change the order of the original elements ,sice the item is pushed from its original/relative positioni.e The space from which the elemnt is pushed top,or left is not occupied
   This only moves the item relative to the oarent it is contained in.
3. absolute: Removes the item with the absolute position from the flow/dom/html view  and  .The position previously occupied by the item is occupied the next items that follow it.
   The item is completely reoved from the dom and floats above it and can be position with top,left etc.The item can be placed anywhere on the view page.e.g top bottom.
   Else it considers the main html element as the  parent.How ever we can put this item in a parent item with a position of relative .Then we can put this absolute item ,relative to that item. i.e Inside the parent item that has any other position aside from relative.
4. fixed : Fixed to a place.An moves as you move while fixed to that place Doesnt give two shits about the parent.It moves as you scroll. Always considers html element as the parent. Stays there when scrolled.
5. sticky : Relative ( when normal) + fixed ( when scrolled). The values for top, right, bottom, left become active when scrolled


E.Gh2 {
  position: absolute;
  left: 100px;
  top: 150px;
}

*               ********** Pseudo selectors **********

*   Pseudo selectors  - This are only two i.e ::before and ::after.
*                     - They add or implement css before and after the selected item  e.g <div> name </div>
*                     - e.g div::after{
*                                content:"**",
*                               background:''red',}
*                               
*                     -   This gives us a result of-  name**          
*                               
*                     - e.g div::before{
*                                content:"**",
*                               background:''red',}
*                               
*                     -   This gives us a result of-  **name   
*                               
*  Attribute selectors     - This is like a selector for elements with the.. data-"" .. atribute.
*                          - We put this data-"" in the elememnt and then in the css we select this element 
*                          - with [] the square brackets. e.g
*                                <div data-book > Name </div>                         
*                        in the css  [data-book]{                                     
*                                     background="red" }
*                          - How ever we can can be specific on which element with the attribiute selector to choose
*                               e.g  <div data-book="name">Name </div>
*                                     [data-book="name"]{
*                                           background:'red'}   
*                               
*                               NOTE--> Its like class selectors but on steroids using [] 
*                               Thsi can be used to select elements with start ,middle and  finishing characters
*                                     start - ^    e.g [data-book^="na"]
*                                     middle - *   e.g [data-book*="am"]     
*                                     finish - $   e.g [data-book^="me"]
*                               
*                               
*                    ********** Transform **********          
*            This can be used to alter the position of a element.
*             It has the folowing :   rotate()           Is used to rotate the component in degrees i..e deg
*                                     scale()            Is used to scale the element
*                                     skew()             Is used to strech the element on the X or Y axis
*                                     translate()        Is used to change the position of an element.You can put the iten you want to translate in a container with relative position and the elemnt to be in abslote position
                                      transform property:The transform property allows you to combine multiple transformation functions together.You can apply multiple transformations by chaining them within the transform property.







The transform property in CSS is used to modify the coordinate space of the CSS visual formatting model, allowing you to rotate, scale, skew, or translate an element. Here's a breakdown of the different functions you asked about:

rotate(): This function is used to rotate an element around a fixed point defined by the transform-origin property. The amount of rotation is specified in degrees.
Example:
    div {
      transform: rotate(45deg);
    }
    ```
In this example, the div element is rotated 45 degrees clockwise.

scale(): This function is used to change the size of an element. It accepts one or two values; if two values are specified, the first sets the scale factor on the x-axis and the second on the y-axis. If only one value is specified, it sets the scale factor on both axes.
Example:
    div {
      transform: scale(2, 3);
    }
    ```
In this example, the div element is scaled to twice its original width and three times its original height.

skew(): This function is used to skew an element along the x and y axes. The amount of skewing is specified in degrees.
Example:
    div {
      transform: skew(20deg, 10deg);
    }
    ```
In this example, the div element is skewed 20 degrees along the x-axis and 10 degrees along the y-axis.

translate(): This function is used to move an element from its current position. It accepts two values representing the translation distances along the x-axis and y-axis.
Example:
    div {
      transform: translate(50px, 100px);
    }
    ```
In this example, the div element is moved 50 pixels to the right and 100 pixels down from its current position.

You can combine multiple transform functions in a single transform property. The functions are applied from right to left.

Example:

div {
  transform: translate(30px, 20px) rotate(20deg);
}
In this example, the div element is first rotated 20 degrees, then shifted 30 pixels to the right and 20 pixels down w3schools.com, developer.mozilla.org.




*                                      
*                     We can also use css variables to change may be one aspect of the transform
*               E.g Here we set the values uin a css variable
*                                                            --> transform: translateY(var(--transy,50px) ) translateX(var(--transx,90px));           
*                   We can change this value by refing to the class with the above characteristic by  
*                                                            --> .big{--transy:90px;}
*                                                                                                      
*                               
*                    ********** CSS variables **********          
*             A css variable starts with two hyphens and then the variable name.Then we give it a normal value like any other css selector.
*             We then refer to the values  in the  css valuables by usin the tag ---> var()   e.g    var(--book)
*                               e.g --kitchen:red
*                                   --book:10px
*
* Now .Where can we apply this css variable. We can use this to store certain variables that we can reuse in the css               
*    we can store this values in e.g :root {}    this is same as the html selector tag                         
*     :root{
*          --div-background:red;
*          --p-color:white;                            
*          }
              
*      P{                         
*        backround:var(--div-background);                       
*        color:var(--p-color);                       
*        }                      
*                               
*         We UPDATE the values in the css variables in the following way.                      
*       p{                        
*         --p-color:green;                      
*        }                       
*                               
*          Now here in this  css variable ,The drop back value is applied if the css varaible is not available
*          Here the value of green s applied as the background since there is no shelf with any value.                     
*              P{                                                
*                 background-color:var(--shelf,green)   }            
*                               
*            We can use this to change the background of our website from light to dark                   
*            Here ,the we set  --website-background css variable to no value but give it a value to drop back to .which will be the lighy theme                    
*            To change the background of the website,we give the  --website-background a value  black ,which which will nullyfy the drop back value of the light theme.                   
*                               
*               heres how we do it in java script.                    
*                               
*                    document.getElementById('dark-theme-btn').addEventListener
*                       ('click',()=>{
*                           document.documentElement.style.setProperty('--website-background','black')
*                       })
*                       
*                       document.getElementById('light-theme-btn').addEventListener
*                       ('click',()=>{
*                           document.documentElement.style.setProperty('--website-background','white')
*                       })
              
*                               
*                               
