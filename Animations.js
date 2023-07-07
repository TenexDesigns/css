CSS animations allow you to animate HTML elements without using JavaScript or Flash. Lets go through the different aspects of CSS animations explained in the code samples provided:

Keyframes and Animation Duration:
To create a CSS animation, you need to define keyframes using the @keyframes rule. Keyframes specify the styles an element will have at certain times. You can define keyframes using percentages (0% to 100%) or specific keywords like from and to. Here's an example that gradually changes the background color of a <div> element from red to yellow over 4 seconds:
css
Copy code
@keyframes example {
  from { background-color: red; }
  to { background-color: yellow; }
}

div {
  width: 100px;
  height: 100px;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
}
Using Keyframes with Percentages:
You can define keyframes using percentage values instead of from and to keywords. This allows you to add as many style changes as you want during the animation. The following example changes the background color of a <div> element at different percentages of the animation:
css
Copy code
@keyframes example {
  0% { background-color: red; }
  25% { background-color: yellow; }
  50% { background-color: blue; }
  100% { background-color: green; }
}

div {
  width: 100px;
  height: 100px;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
}
Animating Multiple Properties:
CSS animations can animate multiple properties simultaneously. In this example, both the background color and position of a <div> element change at different percentages of the animation:
css
Copy code
@keyframes example {
  0% { background-color: red; left: 0px; top: 0px; }
  25% { background-color: yellow; left: 200px; top: 0px; }
  50% { background-color: blue; left: 200px; top: 200px; }
  75% { background-color: green; left: 0px; top: 200px; }
  100% { background-color: red; left: 0px; top: 0px; }
}

div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
}
Delaying an Animation:
You can add a delay before starting an animation using the animation-delay property. In this example, the animation starts after a 2-second delay:
css
Copy code
div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-delay: 2s;
}
Controlling Animation Iteration:
The animation-iteration-count property determines how many times an animation should run. By default, it plays once. You can set it to a specific number or infinite for continuous looping:
css
Copy code
div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-iteration-count: 3;
}
Specifying Animation Direction:
The animation-direction property controls the direction of an animation. It can have values like normal, reverse, alternate, or alternate-reverse. Here are examples of different animation directions:
css
Copy code
div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-direction: reverse;
}

div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-iteration-count: 2;
  animation-direction: alternate;
}

div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-iteration-count: 2;
  animation-direction: alternate-reverse;
}
Timing Function and Fill Mode:
The animation-timing-function property specifies the speed curve of an animation.
  You can use values like ease, linear, ease-in, ease-out, ease-in-out, or cubic-bezier to define custom curves.
  The animation-fill-mode property controls how styles are applied before and after the animation. 
  It can be set to The animation-fill-mode property specifies how an element should be styled before and after the animation plays. It controls the styles applied to the element during the animation delay and after the animation has completed.
There are four possible values for the animation-fill-mode property:

none: This is the default value. It means that no styles are applied to the element before or after the animation. The element will be styled based on its regular CSS rules.

forwards: With this value, the element retains the computed values set by the last keyframe of the animation when the animation ends. In other words, the element will hold the styles defined in the animation's final keyframe. If the animation has a defined animation-direction, the element will retain the styles according to the direction.

backwards: This value causes the element to adopt the styles defined by the first keyframe of the animation during the animation delay period. Once the animation starts, the element will follow the styles defined by the animation as it progresses. If the animation has a defined animation-direction, the element will adopt the styles based on the direction.

both: This value combines the effects of both forwards and backwards. The element will hold the styles defined by the last keyframe when the animation ends and will adopt the styles defined by the first keyframe during the animation delay.

Heres an example that demonstrates the animation-fill-mode property:

css
Copy code
@keyframes example {
  from { background-color: red; }
  to { background-color: yellow; }
}

div {
  width: 100px;
  height: 100px;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-fill-mode: forwards;
}
In this example, the div element starts with a red background color. During the animation, the background color gradually changes to yellow. After the animation ends, the animation-fill-mode: forwards rule causes the element to retain the yellow background color.

You can experiment with different animation-fill-mode values (none, forwards, backwards, both) to control how the element is styled before and after the animation.
