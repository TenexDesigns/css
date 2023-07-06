/*
*                  In this section we are going to talk about pseudo elements and pseudo classes
**                    ********* PSEUDO ELEMENTS **********          
*                              
*  A CSS pseudo-element is a keyword added to a selector that lets you style a specific part of the selected element(s).
*  For example, ::first-line can be used to change the font of the first line of a paragraph.     
*  You can use only one pseudo-element in a selector. It must appear after the simple selectors in the statement.   
*  As a rule, double colons (::) should be used instead of a single colon (:). This distinguishes pseudo-elements from  pseudo-classes .                        
*                    Format----->          
*                         selector::pseudo-element {
*                                 property: value;
*                                                  }      
*                               
*                     Example ----->          
s*                          p::first-line {
*                             color: blue;
*                             text-transform: uppercase;
*                           }     
*                               
*                       Examples of pseudo elemnts        
*      A                  B                C                       F                             G                                                     
*   ::after           ::backdrop        ::cue-region           ::file-selector-button            ::grammar-error Experimental                                                                          
*                     ::before          ::cue                  ::first-line                                                                        
*                                                              ::first-letter                                                   
*     M                  P                  S                                    T                                         
*   ::marker          ::placeholder      ::selection                         ::target-text                                                                         
*                     ::part()           ::slotted()                                                                                      
*                                        ::spelling-error Experimental                                                                                                                                                                                          
*   
*                                       ************** PSEUDO CLASSES ***********                                     
*            Pseudo-classes
*  A CSS pseudo-class is a keyword added to a selector that specifies a special state of the selected element(s). For example,
*  the pseudo-class :hover can be used to select a button when a user's pointer hovers over the button and this selected button can then be styled.                                      
*                  
*                               TYPES OF PSEUDO CLASSES   
*                          
*                1.     *************** USER ACTION PSEUDO-CLASSES ************
*     These pseudo-classes require some interaction by the user in order for them to apply, 
*     such as holding a mouse pointer over an element.                                     
*                                                                        
*                :hover                - Matches when a user designates an item with a pointing device, such as holding the mouse pointer over the item.
*                :active               - Matches when an item is being activated by the user. For example, when the item is clicked on.
*                :focus                - Matches when an element has focus.
*                :focus-visible        - Matches when an element has focus and the user agent identifies that the element should be visibly focused.
*                :focus-within         - Matches an element to which :focus applies, plus any element that has a descendant to which :focus applies.                           
*                                                  
*                                                          
*                 2.     ************** TREE-STRUCTURAL PSEUDO-CLASSES ************
*             These pseudo-classes relate to the location of an element within the document tree.
*
*                :root                 - Represents an element that is the root of the document. In HTML this is usually the <html> element.
*                :empty                - Represents an element with no children other than white-space characters.
*                :nth-child            - Uses An+B notation to select elements from a list of sibling elements.
*                :nth-last-child       - Uses An+B notation to select elements from a list of sibling elements, counting backwards from the end of the list.
*                :first-child          - Matches an element that is the first of its siblings.
*                :last-child           - Matches an element that is the last of its siblings.
*                :only-child           - Matches an element that has no siblings. For example, a list item with no other list items in that list.
*                :nth-of-type          - Uses An+B notation to select elements from a list of sibling elements that match a certain type from a list of sibling elements.
*                :nth-last-of-type     - Uses An+B notation to select elements from a list of sibling elements that match a certain type from a list of sibling elements counting backwards from the end of the list.
*                :first-of-type        - Matches an element that is the first of its siblings, and also matches a certain type selector.
*                :last-of-type         - Matches an element that is the last of its siblings, and also matches a certain type selector.
*                :only-of-type         - Matches an element that has no siblings of the chosen type selector.                                                 
*                                                                        
*                                               
*                 3.      ************* INPUT PSEUDO-CLASSES ***********
*             These pseudo-classes relate to form elements, and enable selecting elements based on HTML attributes and the state that the field is in before and after interaction.  
*                                                          
*                :autofill             - Matches when an <input> has been autofilled by the browser.
*                :enabled              - Represents a user interface element that is in an enabled state.
*                :disabled             - Represents a user interface element that is in a disabled state.
*                :read-only            - Represents any element that cannot be changed by the user.
*                :read-write           - Represents any element that is user-editable.
*                :placeholder-shown    - Matches an input element that is displaying placeholder text. For example, it will match the placeholder attribute in the <input> and <textarea> elements.
*                :default              - Matches one or more UI elements that are the default among a set of elements.
*                :checked              - Matches when elements such as checkboxes and radio buttons are toggled on.
*                :indeterminate        - Matches UI elements when they are in an indeterminate state.
*                :blank                - Matches a user-input element which is empty, containing an empty string or other null input.
*                :valid                - Matches an element with valid contents. For example, an input element with the type 'email' that contains a validly formed email address or an empty value if the control is not required.
*                :invalid              - Matches an element with invalid contents. For example, an input element with type 'email' with a name entered.
*                :in-range             - Applies to elements with range limitations. For example, a slider control when the selected value is in the allowed range.
*                :out-of-range         - Applies to elements with range limitations. For example, a slider control when the selected value is outside the allowed range.
*                :required             - Matches when a form element is required.
*                :optional             - Matches when a form element is optional.
*                :user-invalid         - Represents an element with incorrect input, but only when the user has interacted with it.                                      
*                                                                        
*                                               
*                  4.     ************* LINGUISTIC PSEUDO-CLASSES ************
*              These pseudo-classes reflect the document language and enable the selection of elements based on language or script direction.                            
*                                                          
*                :dir()                 - The directionality pseudo-class selects an element based on its directionality as determined by the document language.
*                :lang()                - Select an element based on its content language                                                
*                                                                        
*                                               
*                  5.    ************** LOCATION PSEUDO-CLASSES **************
*             These pseudo-classes relate to links, and to targeted elements within the current document.                              
*                                                          
*               :any-link               - Matches an element if the element would match either :link or :visited.
*               :link                   - Matches links that have not yet been visited.
*               :visited                - Matches links that have been visited.
*               :local-link             - Matches links whose absolute URL is the same as the target URL. For example, anchor links to the same page.
*               :target                 - Matches the element which is the target of the document URL.
*               :target-within          - Matches elements which are the target of the document URL, but also elements which have a descendant which is the target of the document URL.
*               :scope                  - Represents elements that are a reference point for selectors to match against.

*                 6.      ************** Resource state pseudo-classes ***************
*              These pseudo-classes apply to media that is capable of being in a state where it would be described as playing, such as a video.
*
*               :playing                - Represents a media element that is capable of playing when that element is playing.
*               :paused                 - Represents a media element that is capable of playing when that element is paused.                                                  
*                                                                        
*                7.       ************* TIME-DIMENSIONAL PSEUDO-CLASSES ************
*              These pseudo-classes apply when viewing something which has timing, such as a WebVTT caption track.

*              :current                  - Represents the element or ancestor of the element that is being displayed.
*              :past                     - Represents an element that occurs entirely before the :current element.
*              :future                   - Represents an element that occurs entirely after the :current element.         
*                                                  
*                8.         ************* ELEMENT DISPLAY STATE PSEUDO-CLASSES  *************
*              These pseudo-classes enable the selection of elements based on their display states.                                        
*                                                                      
*              :fullscreen               - Matches an element that is currently in fullscreen mode.
*              :modal                    - Matches an element that is in a state in which it excludes all interaction with elements outside it until the interaction has been dismissed.
*              :picture-in-picture       - Matches an element that is currently in picture-in-picture mode.                                                       
*                                               
*                       ******************** ALPHABETRIC INDEX ******************                           
*                                                          
*      *      A
*      
*      :active                - Matches when an item is being activated by the user. For example, when the item is clicked on.
*      :any-link              - Matches an element if the element would match either :link or :visited.
*      :autofill              - Matches when an <input> has been autofilled by the browser.
*      B
*      
*      :blank (Experimental)  - Matches a user-input element which is empty, containing an empty string or other null input.
*      C
*      
*      :checked                - Matches when elements such as checkboxes and radio buttons are toggled on.
*      :current Experimental   - Represents the element or ancestor of the element that is being displayed.
*      D
*      
*      :default                - Matches one or more UI elements that are the default among a set of elements.
*      :defined
*      :dir() (Experimental)     - The directionality pseudo-class selects an element based on its directionality as determined by the document language.
*      :disabled               - Represents a user interface element that is in a disabled state.
*      E
*      
*      :empty                  - Represents an element with no children other than white-space characters.
*      :enabled                - Represents a user interface element that is in an enabled state.
*      F
*      
*      :first
*      :first-child            - Matches an element that is the first of its siblings.
*      :first-of-type          - Matches an element that is the first of its siblings, and also matches a certain type selector.
*      :fullscreen                    - Matches an element that is currently in fullscreen mode.
*      :future Experimental           - Represents an element that occurs entirely after the :current element.
*      :focus                         - Matches when an element has focus.
*      :focus-visible                 - Matches when an element has focus and the user agent identifies that the element should be visibly focused.
*      :focus-within                  - Matches an element to which :focus applies, plus any element that has a descendant to which :focus applies.
*      H
*      
*      :has() Experimental            - The relational pseudo-class represents an element if any of the relative selectors match when anchored against the attached element.
*      :host
*      :host()
*      :host-context() Experimental
*      :hover                                - Matches when a user designates an item with a pointing device, such as holding the mouse pointer over the item.
*      I
*      
*      :indeterminate                 - Matches UI elements when they are in an indeterminate state.
*      :in-range                      - Applies to elements with range limitations. For example, a slider control when the selected value is in the allowed range.
*      :invalid                       - Matches an element with invalid contents. For example, an input element with type 'email' with a name entered.
*      :is()                          - The matches-any pseudo-class matches any element that matches any of the selectors in the list provided. The list is forgiving.
*       L
*       
*       :lang()                       - Select an element based on its content language.
*       :last-child                   - Matches an element that is the last of its siblings.
*       :last-of-type                 - Matches an element that is the last of its siblings, and also matches a certain type selector.
*       :left
*       :link                          - Matches links that have not yet been visited.
*       :local-link Experimental       - Matches links whose absolute URL is the same as the target URL. For example, anchor links to the same page.
*       M
*       
*       :modal            -Matches an element that is in a state in which it excludes all interaction with elements outside it until the interaction has been dismissed.
*       N
*       
*       :not()                            - The negation, or matches-none, pseudo-class represents any element that is not represented by its argument.
*       :nth-child()                      - Uses An+B notation to select elements from a list of sibling elements
*       :nth-col() Experimental           - 
*       :nth-last-child()                 - Uses An+B notation to select elements from a list of sibling elements, counting backwards from the end of the list.
*       :nth-last-col() Experimental
*       :nth-last-of-type()               - Uses An+B notation to select elements from a list of sibling elements that match a certain type from a list of sibling elements counting backwards from the end of the list.
*       :nth-of-type()                    - Uses An+B notation to select elements from a list of sibling elements that match a certain type from a list of sibling elements.
*       O
*       
*       :only-child                  - Matches an element that has no siblings. For example, a list item with no other list items in that list.
*       :only-of-type                - Matches an element that has no siblings of the chosen type selector.
*       :optional                    - Matches when a form element is optional.
*       :out-of-range                - Applies to elements with range limitations. For example, a slider control when the selected value is outside the allowed range.
*       P
*       
*       :past (Experimental)         - Represents an element that occurs entirely before the :current element.
*       :picture-in-picture          - Matches an element that is currently in picture-in-picture mode.
*       :placeholder-shown           - Matches an input element that is displaying placeholder text. For example, it will match the placeholder attribute in the <input> and <textarea> elements.
*       :paused                      - Represents a media element that is capable of playing when that element is paused.
*       :playing                     - Represents a media element that is capable of playing when that element is playing.
*       R
*       
*       :read-only                   - Represents any element that cannot be changed by the user.
*       :read-write                  - Represents any element that is user-editable.
*       :required                    - Matches when a form element is required.
*       :right
*       :root                        - Represents an element that is the root of the document. In HTML this is usually the <html> element.
*       S
*       
*       :scope                       - Represents elements that are a reference point for selectors to match against. 
*       :state() (Experimental)
*       T
*       
*       :target                         - Matches the element which is the target of the document URL.
*       :target-within (Experimental)   - Matches elements which are the target of the document URL, but also elements which have a descendant which is the target of the document URL.
*       U
*       
*       :user-invalid (Experimental)     - Represents an element with incorrect input, but only when the user has interacted with it.
*       V
*       
*       :valid                        - Matches an element with valid contents. For example, an input element with the type 'email' that contains a validly formed email address or an empty value if the control is not required.
*       :visited                      - Matches links that have been visited.
*       W
*       
*       :where()                      - The specificity-adjustment pseudo-class matches any element that matches any of the selectors in the list provided without adding any specificity weight. The list is forgiving.        
*           
*/
