const pekes = document.querySelectorAll('.peke')//get all the pekes

const getPlayer = (peke) => {
    return peke.getAttribute('player');
}

const getNextRow = (gap) => {
    // ......returns next_row
    row = gap.parentElement;//get the row in which the gap lies
    id = row.id;//get current row id
    i = id.split('_')[1];//split the id to get the number
        
    if(player == 'pa'){//if the player is Player A, incrament the row id and get the id of the next row
        nid = 'r_' + (parseInt(i)+1)
    }else if(player == 'pb'){//else if the player is Player B decreament the row id to get the id of the next row 
        nid = 'r_' + (parseInt(i)-1)
    }
    next_row = document.getElementById(nid)//now get the next row where the dragged peke can find new placements

    return next_row
}
const getPossibleGaps = (curent_gap, peke) => {
    ci = parseInt(get_child_index(curent_gap));// get the index of the current parent gap
    valid_gaps = new Array;//initiate an empty array for valid gaps
    if(ci > 0 && ci < 7){// if the gap is not the first pr last in the row then get two valid gaps
        pg1 = getNextRow(curent_gap).children[ci + 1];//the first gap
        pg2 = getNextRow(curent_gap).children[ci - 1];//the second gap
        // create an array and push this gaps then give then a class name//
        if(pg1.innerHTML == ''){//if the gap is empty then add the valid class name;
            valid_gaps.push(pg1);
        }else{}

        if(pg2.innerHTML == ''){//if the gap is empty then add the valid class name
            valid_gaps.push(pg2)
        }else{}
        
    }else if(ci == 0){//if the gap is the first in the row then return the gap to right in the next row
        pg = getNextRow(curent_gap).children[ci + 1]
        if(pg.innerHTML == ''){//also add the valid class if the gap is empty
            valid_gaps.push(pg);
        }else{}
    }else if(ci == 7){//if the gap is the last, then return the gap on the left in the next row
        pg = getNextRow(curent_gap).children[ci - 1]
        if(pg.innerHTML == ''){//similaly if the the gap is empty then add the valid class
            valid_gaps.push(pg);
        }else{}
    }

    for(gap of valid_gaps){
        if(gap.matches('valid')){

        }else{
            gap.classList.add('valid')
        }
    }

    const possibleMoves = document.querySelectorAll('.valid')
    for(const pgap of possibleMoves){
        pgap.addEventListener('dragover', dragOver);
        pgap.addEventListener('dragenter', dragEnter);
        pgap.addEventListener('dragleave', dragLeave);
        pgap.addEventListener('drop', () => {
            pgap.append(peke);
            pgap.classList.remove('hovered');
        });
    }
}

//loop through the pekes
for(const peke of pekes){
    const tar = peke
    const par = peke.parentElement; //get the current gap of the dragged peke
    
    tar.ondragstart = (e) => {//listen for the drag event on any peke
        tar.style.borderRadius = '50%'
        player = getPlayer(peke)//get the player who owns the dragged peke
        setTimeout(() => par.innerHTML = '', 0)// set gap empty after the peke has been dragged out
        //--------------------------------------------------------------------------------------------------------------//

        next_row = getNextRow(par);
        //-------------------------------------------------------------------------------------------------------------//

        // getPossibleGaps(curent_gap)............just prepare all the valid gaps to recieve the peke but should follow the protocol
        getPossibleGaps(par, tar);

        // console.log(getPossibleGaps(par))//console to test
    }

    tar.ondragend = (event) =>{//after the drag
        
    }
    
}

const removeClass = (className) =>{
    vgaps = document.querySelectorAll(className);
    console.log(vgaps.length)
    for(g of vgaps){
        g.classList.remove(className)
    }
    vgaps = document.querySelectorAll(className);
    if(vgaps.length > 0){
        removeClass(className)
    }else{
        console.log(vgaps.length)
    }
}

// this takes in a child node then finds its index in its parent node
function get_child_index(child) {
    cs = child.parentElement.children// get all the siblings to the child
    index = undefined//declare the index and set it to undefined
    for(c in cs){// loop through all the children until we find a child that is equal to the child
        tar = cs[c]
        if(tar == child){
            index = c;
            break;
        }
    }

    return index
}

function dragOver(e){
    e.preventDefault();    
    console.log('over')
}

function dragEnter(e){
    e.preventDefault();
    this.classList.add('hovered');
}

function dragLeave(){
    this.classList.remove('hovered');
    console.log('leave')
}

// function drop(){
//     peke = document.createElement('div')
//     peke.setAttribute('player', 'pa')          

//     this.append(peke)
    
//     console.log('drop')
// }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//              
//                      SECOND ATTEMPT!
//
//
class State{
    constructor(player){
        this.player = player;
    }

    html = () => {
        peke = document.createElement('div')
        peke.setAttribute('player', this.player);
        peke.className = 'peke';
        peke.setAttribute('draggable', true);

        return peke;
    }

}

const hosts = document.querySelectorAll('.host')
const pekes = document.querySelectorAll('.peke');

//drop events
for(host of hosts){
    host.addEventListener('dragover', dragOver)
    host.addEventListener('dragenter', dragEnter)
    host.addEventListener('dragleave', dragLeave)
    host.addEventListener('drop', drop)
}

// drag events
for(peke of pekes){
    peke.addEventListener('dragstart', dragStart);
    peke.addEventListener('dragend', dragEnd);
}

//peke functions
function dragStart(x){
    node = this;
    this.className = 'hold';
    next_row = getNextRow(x.path[1])
    child_index = get_child_index(x.path[1])
    setValidGaps(next_row,child_index, getPlayer(this))
    setTimeout(() => this.className = 'invicible', 0)
    console.log(child_index, next_row)
}

function dragEnd(e){
    this.className = 'peke';
    // e.path[1].innerHTML = ''
}

//host functions
function dragOver(e){
    e.preventDefault();
}

function dragEnter(e){
    e.preventDefault();
    if(this.matches('valid')){
        this.className += ' hovered';
    }
}

function dragLeave(){
    this.classList.remove('hovered')
}

function drop(){
    if (this.matches('valid')){
        console.log('recieved')
    }
    this.classList.remove('hovered')
    this.classList.remove('valid')
}

const getNextRow = (gap) => {
    // ......returns next_row
    row = gap.parentElement;//get the row in which the gap lies
    id = row.id;//get current row id
    i = id.split('_')[1];//split the id to get the number
    player = gap.children[0].getAttribute('player');
    if(player == 'pa'){//if the player is Player A, incrament the row id and get the id of the next row
        nid = 'r_' + (parseInt(i)+1)
    }else if(player == 'pb'){//else if the player is Player B decreament the row id to get the id of the next row 
        nid = 'r_' + (parseInt(i)-1)
    }
    next_row = document.getElementById(nid)//now get the next row where the dragged peke can find new placements

    return next_row
}

// this takes in a child node then finds its index in its parent node
function get_child_index(child) {
    cs = child.parentElement.children// get all the siblings to the child
    index = undefined//declare the index and set it to undefined
    for(c in cs){// loop through all the children until we find a child that is equal to the child
        tar = cs[c]
        if(tar == child){
            index = c;
            break;
        }
    }

    return parseInt(index)
}

function setValidGaps(next_row, child_index, player){
    if(child_index > 0 && child_index < 7){
        if(player == 'pa'){
            vg1 = next_row.children[child_index + 1]
            vg1.className += ' valid';
        }
        
    }
    
}

const getPlayer = (peke) => {
    return peke.getAttribute('player');
}


 ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        //                      HELPER FUNCTIONS
        function setId(str, i){
            return str + '_' + i;
        }
        function getInt(str){
            i = str.split('_')[1];
            if(isNaN(i)){
                return undefined;
            }else{
                return parseInt(i);
            }
        }
        function getChildIndex(child) {
            cs = child.parentElement.children// get all the siblings to the child
            index = undefined//declare the index and set it to undefined
            for(c in cs){// loop through all the children until we find a child that is equal to the child
                tar = cs[c]
                if(tar == child){
                    index = c;
                    break;
                }
            }
            return parseInt(index)
        }
        function getNextRow(gap){
            row = gap.parentElement;//get the row in which the gap lies
            id = row.id;//get current row id
            i = id.split('_')[1];//split the id to get the number
            player = gap.children[0].getAttribute('player');
            if(player == 'pa'){//if the player is Player A, incrament the row id and get the id of the next row
                nid = 'r_' + (parseInt(i)+1)
            }else if(player == 'pb'){//else if the player is Player B decreament the row id to get the id of the next row 
                nid = 'r_' + (parseInt(i)-1)
            }
            next_row = document.getElementById(nid)//now get the next row where the dragged peke can find new placements

            return next_row
        }
        function moveOptions(curent_gap){
            row = getNextRow(curent_gap)
            curent_gap_index = getChildIndex(curent_gap)
            gaps = new Array;
            if(curent_gap_index > 0 && curent_gap_index < 7){
                valid_gap_1 = row.children[curent_gap_index + 1];
                valid_gap_2 = row.children[curent_gap_index - 1];
                if (empty(valid_gap_1)){gaps.push(valid_gap_1);}else{}
                if(empty(valid_gap_2)){gaps.push(valid_gap_2);}else{}
                
            }else if (curent_gap_index == 0){
                valid_gap = row.children[1];
                if(empty(valid_gap)){gaps.push(valid_gap)}else{};
            }else if(curent_gap_index == 7){
                valid_gap = row.children[6];
                if(empty(valid_gap)){gaps.push(valid_gap)}else{}
            }
            return gaps
        }
        function empty(gap){
            return gap.children.length == 0
        }
        function init(){
            const hosts = document.querySelectorAll('.host')
            for(const host of hosts){
                if(empty(host)){
                    host.classList.add('empty');
                }else{}
            }
        }