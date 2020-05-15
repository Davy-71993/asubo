
$(document).ready(function(){
    openNewGame();
})
class Peke{
    constructor(player){
        this.player = player;
    }
    create = () => {
        const div = document.createElement('div');
        div.className = 'peke';
        div.setAttribute('player', this.player);
        div.setAttribute('onclick', 'javascript:setToMove(this)');
        div.setAttribute('ondragstart', 'javascript:setToMove(this)')
        div.draggable = true;

        return div;
    }
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                      START THE GAME.
function openNewGame(){
    const pa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    const pb = [32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21];
    const empties = [13, 14, 15, 16, 17, 18, 19, 20];
    for(const i of pa){
        gap = document.getElementById(setId('g', i));
        peke = new Peke('pa');
        gap.innerHTML = peke.create().outerHTML;
    }

    for(const i of pb){
        gap = document.getElementById(setId('g', i));
        peke = new Peke('pb');
        gap.innerHTML = peke.create().outerHTML
    }

    for(const em of empties){
        document.getElementById(setId('g', em)).innerHTML = '';
    }

    init();
    localStorage.removeItem('state');
    localStorage.removeItem('player');
    
}
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                      INITIATE A MOVE
function setToMove(target){
    if(canMove(target.getAttribute('player'), target.parentElement.id)){
        curent_gap = target.parentElement;
        curent_gap_id = curent_gap.id;
        player = target.getAttribute('player')

        localStorage.setItem('curent_gap', curent_gap_id);
        localStorage.setItem('player', player);

        console.log(validgaps(curent_gap_id, player))
        
    }else{console.log('This Peke can not move!');}
    
}
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                      MAKE A MOVE
const hosts = document.querySelectorAll('.host');
for(const host of hosts){
    host.addEventListener('click', moveHere);
    host.addEventListener('dragover', dragOver);
    host.addEventListener('dragenter', dragEnter);
    host.addEventListener('dragleave', dragLeave);
    host.addEventListener('drop', moveHere);
}
function moveHere(){
    player = localStorage.getItem('player');
    last_gap = localStorage.getItem('curent_gap');
    id = this.id
    if(player && last_gap){
        if(validgaps(last_gap,player).includes(id)){
            peke = new Peke(player);
            this.append(peke.create())
            document.getElementById(last_gap).innerHTML = '';
            init();
            // localStorage.removeItem('player');
            // localStorage.removeItem('curent_gap');
            localStorage.setItem('state', document.querySelector('.draft').innerHTML);
        }
    }else{
        console.log('There is no peke ready to be moved, please select one and try again')
    }
}
function dragOver(e){e.preventDefault()}
function dragEnter(e){
    e.preventDefault(); 
    player = localStorage.getItem('player');
    last_gap = localStorage.getItem('curent_gap')
    if (validgaps(last_gap, player).includes(this.id)){
        this.classList.add('hovered')
    }
}
function dragLeave(){this.classList.remove('hovered')}
//
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                      HELPER FUNCTIONS
function validgaps(gap_id, player){
    gaps = [];
    empties = [];

    switch (gap_id) {
        case 'g_1':
            if(player == 'pa'){
                gaps.push('g_5','g_6')
            }else{}
            break;

        case 'g_2':
            if(player == 'pa'){
                gaps.push('g_6','g_7')
            }else{}
            break;
        case 'g_3':
            if(player == 'pa'){
                gaps.push('g_7','g_8')
            }else{}
            break;
        case 'g_4':
            if(player == 'pa'){
                gaps.push('g_8')
            }else{}
            break;
        case 'g_5':
        if(player == 'pa'){
                gaps.push('g_9')
            }else{
                gaps.push('g_1')
            }
            break;
        case 'g_6':
            if(player == 'pa'){
                gaps.push('g_10','g_9')
            }else{
                gaps.push('g_1', 'g_2')
            }
            break;
        case 'g_7':
            if(player == 'pa'){
                gaps.push('g_10','g_11')
            }else{
                gaps.push('g_2', 'g_3')
            }
            break;
        case 'g_8':
            if(player == 'pa'){
                gaps.push('g_11','g_12')
            }else{
                gaps.push('g_4', 'g_3')
            }
            break;
        case 'g_9':
            if(player == 'pa'){
                gaps.push('g_14','g_13')
            }else{
                gaps.push('g_6', 'g_5')
            }
            break;
        case 'g_10':
            if(player == 'pa'){
                gaps.push('g_14','g_15')
            }else{
                gaps.push('g_7', 'g_6')
            }
            break;
        case 'g_11':
            if(player == 'pa'){
                gaps.push('g_15','g_16')
            }else{
                gaps.push('g_8', 'g_7')
            }
            break;
        case 'g_12':
            if(player == 'pa'){
                gaps.push('g_16')
            }else{
                gaps.push('g_8')
            }
            break;
        case 'g_13':
            if(player == 'pa'){
                gaps.push('g_17')
            }else{
                gaps.push('g_9')
            }
            break;
        case 'g_14':
            if(player == 'pa'){
                gaps.push('g_18','g_17')
            }else{
                gaps.push('g_9', 'g_10')
            }
            break;
        case 'g_15':
            if(player == 'pa'){
                gaps.push('g_18','g_19')
            }else{
                gaps.push('g_10', 'g_11')
            }
            break;

        case 'g_16':
            if(player == 'pa'){
                gaps.push('g_19','g_20')
            }else{
                gaps.push('g_11', 'g_12')
            }
            break;
        case 'g_17':
            if(player == 'pa'){
                gaps.push('g_21','g_22')
            }else{
                gaps.push('g_14', 'g_13')
            }
            break;
        case 'g_18':
            if(player == 'pa'){
                gaps.push('g_22', 'g_23')
            }else{
                gaps.push('g_14', 'g_15')
            }
            break;
        case 'g_19':
            if(player == 'pa'){
                gaps.push('g_23', 'g_24')
            }else{
                gaps.push('g_16', 'g_15')
            }
            break;
        case 'g_20':
            if(player == 'pa'){
                gaps.push('g_24')
            }else{
                gaps.push('g_16')
            }
            break;
        case 'g_21':
            if(player == 'pa'){
                gaps.push('g_25')
            }else{
                gaps.push('g_17')
            }
            break;
        case 'g_22': 
            if(player == 'pa'){
                gaps.push('g_26','g_25')
            }else{
                gaps.push('g_17', 'g_18')
            }
            break;
        case 'g_23':
            if(player == 'pa'){
                gaps.push('g_27','g_26')
            }else{
                gaps.push('g_19', 'g_18')
            }
            break;
        case 'g_24':
            if(player == 'pa'){
                gaps.push('g_28','g_27')
            }else{
                gaps.push('g_20', 'g_19')
            }
            break;
        case 'g_25':
            if(player == 'pa'){
                gaps.push('g_30','g_29')
            }else{
                gaps.push('g_22', 'g_21')
            }
            break;
        case 'g_26':
            if(player == 'pa'){
                gaps.push('g_30', 'g_31')
            }else{
                gaps.push('g_23', 'g_22')
            }
            break;
        case 'g_27':
            if(player == 'pa'){
                gaps.push('g_32', 'g_31')
            }else{
                gaps.push('g_24', 'g_23')
            }
            break;
        case 'g_28':
            if(player == 'pa'){
                gaps.push('g_32')
            }else{
                gaps.push('g_24')
            }
            break;
            case 'g_29':
            if(player == 'pa'){
                
            }else{
                gaps.push('g_25')
            }
            break;
        case 'g_30':
            if(player == 'pa'){

            }else{
                gaps.push('g_26', 'g_25')
            }
            break;
        case 'g_31':
            if(player == 'pa'){
                
            }else{
                gaps.push('g_27', 'g_26')
            }
            break;
        case 'g_32':
            if(player == 'pa'){
                
            }else{
                gaps.push('g_28', 'g_27')
            }
            break;

        default:
            break;
    }

    for(const gap of gaps){
        elm = document.getElementById(gap)
        if(elm.innerHTML == ''){
            empties.push(gap)
        }else{}
    }

    return empties;
}
function canMove(player, gap_id){
    options = validgaps(gap_id, player);
    return options.length > 0;
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
function init(){
    const hosts = document.querySelectorAll('.host');
    for(const host of hosts){
        if (host.innerHTML == ''){
            host.className = 'draft-gap host empty';
        }else{
            host.className = 'draft-gap host covered'
        }
    }

    localStorage.removeItem('curent_gap');
}