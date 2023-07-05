/*  
      <!----- ***** Flex Box ***** ------!>
     Flex box is a display typethat helps us craft css layouts
      much easier

      div{
            dispaly:flex
         }

    A flex box has  a flex container and flex items 

   .     ____________________________________________ 
        |   _________    _________    _________      | <----- flex container  
        |  | flex    |  |  flex   |  | flex    |     |
        |  |__item___|  |__item___|  |__item___|     | 
        |____________________________________________|
     
     -The default behaviour of flex items in a flex container is that
      they start from left to right i.e the flex direction is row 

      Flex container                          Flex item
       --dispaly                              --order
       --flex-direction                       --flex grow
       --flex-wrap                            --flex shrink
       --flex-flow                            --flex basis
       --justify-content                      --flex
       --align-items                          --align-self
       --align-content


      <!-------***** The main axis and cross axis ***** -------!> 

      Knowing the direction of the main axis helps in
       determinig some properties of the flex container and direction of flow of flex items

.                       
.         ______________|______________________________
.        |   _________  |  _________    _________     |         
.        |  | flex    | ||  flex   |  | flex    |     |
.        |  |__item___| ||__item___|  |__item___|     | 
.        |______________|_____________________________|
.                       |
.       -------------------------------------------------->   <----- main axis               |
.                       | 
.                       |
.                       v  <----- cross axis 


.  The main axis is the direction on which  the flex items are laid out
.  The cross axis is determined by the main axis in that the cross axis is perpendicular to the main axis
.  The main axis is determined by the flex direction
.
.        flex-direction:row;   --|----->  main axix                   flex items flow in a row    iiiiii
.                                |
.                                v cros axis        
.
.         flex-direction:column;  --|----->  cros axis                flex items flow in a column   i
.                                   |                                                               i
.
.                                   v main axis                                                     i
.
.
.
.                             <! ----- ****** Flex wrap ***** -----!>

.              The flex wrap make the flex items not fitting on the container
.               to go to the next line instread of squizing or necessating a scroll bar for items to be seen .
.
.                  div{ 
.                    Flex-wrap:wrap;                                   -- So that the flex items that dont fit are pushed to the next line instead
.                     }
.
.
.                               <! ------ ***** Flex flow ***** --------!>
.         
.                         This combines both the properties of  flex direction and flex wrap 
.                         This is the same                                As this

.                         div{                                   div{                                         
.                             flex-flow:row wrap                      flex-wrap:wrap; 
.                            }                                        flex-direction:column;
.                                                                    }
.
.                                <! ----- Justify content -------!>

.                This determines how space along the main axis is used up
.                
.                   Justify-content:flex-start                  This places the flex items on the start of the main axis . This is usually the default.That is why flex items start from the top left
.                   Justify-content:flex-end                    This places the flex items on the end of the main axis
.                   Justify-content:space-between               This places space between the flex items 
.                   Justify-content:space-around                This places space around the flex items 
.                   Justify-content:space-evenly                This places space evenly around the flex items 
.
.
.
.                               <! -------- Align items ------- !>

.                    The align items is all about how we space items along the cross axis
.                    Think of align items as the justify content version of the cross axis
.                     The default alighn item value is usually stretch  .This usally stratsce the flex items          
.                      
.                                  align-items: strech;      This usually strectces the align items from the start of of cross axis to end or in all directions 
.                                  align-items: center;      This usally centers the flex items on the cross axis
.                                  align-items: flex-start;  This usally fixes the flex items on the start of the cross axis
.                                  align-items: flex-end;    This usually fixes the flex items on the end of the cros axis  
.                                  align-items: baseline;    This usually fixes the flex items according to their base lines
.
.
.
.                                          <! -------- Align content ------- !>

.                              This usually aligns the content/flex items within the flex container
.
.                                  align-content: flex-start;        This usally makes all rows of flex items in the container be pushed to the top of the container with no spacing between the rows 
.                                  align-content: flex-end;          This usally makes all rows of flex items in the container be pushed to the bottom of the container with no spacing between the rows                  
.                                  align-content: space-between;     This usually puts space between rows of flex items in the container
.                                  align-content: space-around;      This usually puts space around row of flex items in the container
.                                  align-content: space-around;      This usually puts even space around row of flex items in the container
.                                  align-content: center;            This usally centers the  rows of flex items in the container
.
.                      
.                                     <! -------- ORDER ------- !>
.
.                        This determines the arrangement or order of flex items
.                        The default order is that of the souce code i.e first item in sorce code is the first to be rendered .first come first serve
.                        The ORDER is changed in that the FLEX ITEM with the HIGHEST ORDER NUMBER gets SERVED LAST/ gets pushed the farthest
.                        and the FLEX ITEM with the LOWEST ORDER NUMBER gets SERVED FIRST. note even negative numbers are included.i.e -2 is lower than 2
.                                 e.g p{                      h{                       div{
.                                         order:10                order:2                    order:7
.                                      }                        }                          }
.
.                                           ____________________________________________ 
.                                          |   _________    _________    _________      |        <----- flex container  
.                                          |  | <h>     |  | <div>   |  | <p>     |     |        <p> ,<div>,<h> are the flex items
.                                          |  |_________|  |_________|  |_________|     | 
.                                          |____________________________________________|
.
.
.                                                <!------ ***** Flex  grow **** ---- !>
.
.                                  This dictates how flex items grow to fit in the extra space left in a container
.                                  The default flex grow number is 0 - meanig flex item should no grow to fit into the extra space
.                                  When the flex items have equal numbers,Theis means that the items should grow equaly and distribute the exta space equaly
.                                  The higher the number the more the  space a flex item occupys
.                                  Here below The h1 fits in twice the space of div
.                                  If the numbers are equal Then the flex item occupy equal space
.
.                                            div{                           h1{
.                                                 flex-grow:1                     flex-grow:2;
.                                                }                              } 
.
.
.
.                                       <!------ **** Flex basis ***** ------!>

.                                flex- basis is used to determine the width of flex items
.                                The flex basisspecifies the initial length of a flexible item.
.                                There is and order of importance between selectors that deytermine the width of a flex item
.                                This means that  flex-basis overides width and that max/min-width overides flex basis and width 
.
.                                width                          1 point              
.                                flex-basis                     10 points
.                                max-width/min-width            100 points
.
.
.
.                                            <! ---- **** Flex ***** ------ !>

.                                      This combines flex grow,flex -shrink and flex basis all in one
.
.                                             flex: 1,0,200px
.
.                                     This is the same as flex-grow:1
.                                                         flex-shrink:0;
.                                                         flex-basis:200px;
.
.
.                                    e.g flex:1 1 0;  This means that the flex items grow and shrink
.                                          equally at the same rate and the flex-basis not be used,
.
.                                 <!------------- Align self -------!>
.                      This targets pecificaly only one flex item 
.                       and applies alignment properties on it 
.                         
.                                  align-self: strech;      This usually strectces the align items from the start of of cross axis to end or in all directions 
.                                  align-self: center;      This usally centers the flex items on the cross axis
.                                  align-self: flex-start;  This usally fixes the flex items on the start of the cross axis
.                                  align-self: flex-end;    This usually fixes the flex items on the end of the cros axis  
.                                  align-self: baseline;    This usually fixes the flex items according to their base lines
.
.
.
.
.
.                                        <!---------- CSS GRID --------!>
.                         
.
.                                   ____________________________________________ 
.                                  |   _________    _________    _________      | <----- Grid container  
.                                  |  |         |  |         |  |         |     |
.                                  |  |__item___|  |__item___|  |__item___|     | 
.                                  |____________________________________________|
.
.                                    CONTAINER                        ITEMS
.                            --  grid-templete-columns                -- grid-column-start
.                            --  grid-templete-rows                   -- grid-column-end
.                            --  grid-templete-areas                  -- grid-row-start
.                            --  grid-templete                        -- grid-row-end
.                            --  grid-column-gap                      -- grid-column
.                            --  grid-row-gap                         -- grid-row
.                            --  grid-gap                             -- grid-area
.                            --  grid-auto-columns                    -- justify-self
.                            --  grid-auto-rows                       -- alighn-self
.                            --  grid-auto-flow                       -- place-self
.                            --  grid                                 --
.                            --  justify-content                      --
.                            --  justify-items                        --
.                            --  place-items                          --
.                            --  place-content                        --
.                            --  align-content                        --
.                           
.      

.                              The css grid is amde up of column lines and row lines
.                              The horizontal lines are the row grid lines
.
.                                         ______________________________      <----- Row grid lines
.                                        |____|____|____|____|____|____|        
.                                        |____|____|____|____|____|____|         
.                                        |____|____|____|____|____|____|      <------ Row grid lines   
.                                        |____|____|____|____|____|____|   
.                                             ^
.                                             | column grid lines
.
.
.
.
.
.
.
.
.
.
.


   
   This fiting is dictate by the  number.
   The higher the number the more the  space a flex item occupys
   Here below The h1 fits in twice the space of div
   If the numbers are equal Then the flex item occupy equal space

   .div{                           h1{
        flex-grow:1                     flex-grow:2;
       }                              } 
 
     <! ----- ***** Flex Shrink **** -----!>

     This dictate how flex items in a flex container shrink
     The higher the number ,the  more the item shrinks
     The h1 shrinks twice as fast as the div

     .div{                           h1{
        flex-shrink:1                     flex-shrink:2;
       }                              } 


       <! ----- ****** Flex wrap ***** -----!>

       So the flex wrap make the flex items not fitting on the container
       to go to the next line instread of squizing or necessating a scroll bar for items to be seen .

div{ 
       Flex-wrap:wrap;                                   -- So that the flex items that dont fit are pushed to the next line instead
       flex-grow:1;                                      -- This makes the flex item pushed to the next line , to occpy or grow to occouy the full width of the container
         
         .div{                           h1{
        flex-shrink:1                     flex-shrink:2;
       }                              } 
    }

        <!------ **** Flex basis ***** ------!>
        This is the same as min-width in that thay give the minimun
        width of the flex item,

        Note.
        When we apply flex grow(which makes flex items occupy wntire lenght of container)
        When we apply flex grow of 1 ,with min-width,the flex items all occypy equal portions of the container,irregarledres of the flex items min lenght
         When we apply flex grow with flex basis ,the flex items now occupy the container nased on their width/flexbasis 
        but min width remains stagnat and gives scroll bar if screen is small
        bt flex basis does not give scroll bar and flex items  continue to shrink
 
       Note .This is all done when flex container is in flex-wrap:wrap;
       and all flex item have  flex-grow:1;


       <! ---- **** Flex ***** ------ !>
       This combines flex grow,flex -shrink and flex basis all in one

       flex: 1,0,200px

       This is the same as flex-grow:1
                           flex-shrink:0;
                           flex-basis:200px;


        e.g flex:1 1 0;  This means that the flex items grow and shrink
                         equally at the same rate and the flex-basis not be used,


                         <<<  ---- CSS GRID ----- >>>
                         


        <! ------ **** Css Grid *** ----!>
        This is able by using the dispaly type of grid 
        div{
            display: grid;
        } 


        To make the grids visible we use grid-templete-columns and grid-templete-rows

        There are three ways of  dictating how grids rows and columns  apprear



        1. Fractions   -- e.g  grid-template-columns: 1fr 2fr 1fr; 
   

         This divides the grid in three with 2fr being larger
         - Fraction --- grid-template-columns: 1fr 2fr 1fr;

          div{                                      
            display: grid;
            grid-template-columns: 1fr 2fr 1fr;
        }
         
          1fr   2fr     1fr
        ____________________
        |____|________|____|
        |____|________|____| 
        |____|________|____|
        |____|________|____|

       Note> The same applies for grid-templete-rows


         
        2. Repeat  --- e.g   grid-template-columns: repeat(5,1fr);

        This divides the grid into five equal colums 
          - repeadt --- grid-template-columns: repeat(5,1fr);

           div{                                      
            display: grid;
            grid-template-columns: repeat(5,1fr);
        }
          1fr  1fr  1fr 1fr  1fr
        _________________________
        |____|____|____|____|____|
        |____|____|____|____|____| 
        |____|____|____|____|____|
        |____|____|____|____|____|

       Note> The same applies for grid-templete-rows

   

        3.Percentage    --   e.g  grid-template-columns: 50% 30% 20%

        This divides the grid into three with 50% being the largest colun
        - Percentage --- grid-template-columns: 50% 30% 20%;

         div{                                      
            display: grid;
            grid-template-columns: 50% 30% 20%;
        }
        _____50%_____----30%--_20%_
         ___________________________
        |___________|________|____|
        |___________|________|____| 
        |___________|________|____|
        |___________|________|____|

        The same applies for grid-templete-rows


       
    



          Note- This grids apear to hold elemnts within the wrpper element i.e div
          This div might have nine p elements,Therefore the grid will have three colums (due to 1fr,2fr,1fr) and three rows ,due to ...
            three elemts filling the three coluns and the extra being pushed down  and so on. 
                  
        div{                                      
            display: grid;
            grid-template-columns: 1fr 2fr 1fr;
        }  
         ___1fr__------2fr--------____1fr___
         ___________________________________
        |__<p>___|_____<p>________|__<p>___|
        |__<p>___|_____<p>________|__<p>___|
        |__<p>___|_____<p>________|__<p>___|
       
      
    
       



        <! ---- **** Grid Lines **** ---- !>

        This help us in positioning the element in the grid
        The grid lines are the  lines in this grid.i.e column grid lines and row grid lines
        Their number is plus one the number of columns or the number of rows i.e
           column grid lines = no.Columns+1 
           row grid lines = no.rowss+1 
            
          1    2    3    4    5    6         <------ Number of columns
         ______________________________
        |____|____|____|____|____|____|        
        |____|____|____|____|____|____|         
        |____|____|____|____|____|____|         
        |____|____|____|____|____|____|         
        
        1    2    3    4    5    6    7       <-----   Number of column grid lines.

        The same applies for rows and row grid lines
        I.e We have  4 rows and 5 row grid lines


        ------ Positioning Elemnts using Grid Lines -----
        We use column grid lines to help position an element in the grid based on the colums
    .                                    This can also be written as
        grid-column-start:1           |  grid-column:1/3
        grid-column-end:3             |

        Here The p element starts from the first column grid line and ends in the third column  grid line

        1    2    3    4    5    6    7
         ______________________________
        |____<p>__|____|____|____|____|
        |____|____|____|____|____|____| 
        |____|____|____|____|____|____|
        |____|____|____|____|____|____|

        <!---------------The same is done for row----------1>
      
        We use row grid lines to help position an element in the grid based on the rows
                                          
       .                               This can also be written as
        grid-row-start:2          |  grid-row:2/5
        grid-row-end:5            |

        Here The p element starts from the second row grid line and ends in the fifth row  grid line

       
        1          _____________________________
        2         |____|____|____|____|____|____|
        3         |    |____|____|____|____|____| 
        4         |<p> |____|____|____|____|____|
        5         |____|____|____|____|____|____|







         ______________________________
        |____|____|____|____|____|____|
        |____|____|____|____|____|____| 
        |____|____|____|____|____|____|
        |____|____|____|____|____|____|
   
     
   
   
   */

   *{
    font-family: 'verdana';
    margin: 0;
   }
   body{
    background: #eee;
   }




.wrapper{
    width: 100%;
    max-width: 1060px;
    margin: 0 auto;
    border: 3px solid black;
    
   

}
.flex-container{
    display: flex;
    background-color: #676789;
    flex-wrap:wrap;
}

.box{
    height: 100px;
    border: 3px solid yellow;
    flex: 1,0,200px;
}

.one{
    background: red;
}
.two{
    background: green;


}
.three{
    background: blue;


}
