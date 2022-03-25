(function(){

    const websocket = new WebSocket("ws://localhost:8765");
    websocket.onopen = () => {
        addWebsocketEvents();
        retrieveGrid();
    }

    let canvasDiv = document.querySelector("#canvasDiv");
    let canvas = document.createElement('canvas')
    canvasDiv.appendChild(canvas);

    let ctx = canvas.getContext('2d');
    let gridXCount = 0;
    let gridYCount = 0;
    let offsetX = 0;
    let offsetY = 0;
    let imageSizeX = 0;
    let imageSizeY = 0;

    let x = 0;
    let y = 0;
    let f = 'NORTH';

    let arrowWest = document.getElementById("arrow-west");
    let arrowEast = document.getElementById("arrow-east");
    let arrowSouth = document.getElementById("arrow-south");
    let arrowNorth = document.getElementById("arrow-north");

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight

    //
    // setGridData("GRID:5,5");
    // drawGrid()
    //
    // setState('STATE:0,2,NORTH')
    // drawState()
    // // setState('STATE:1,2,NORTH')
    // // drawState()
    // //

    function addWebsocketEvents() {
        websocket.addEventListener("message",({data})=>{
            if(data.indexOf('GRID:')>=0){
                setGridData(data);
                drawGrid()
            }
            if(data.indexOf("STATE:")>=0){
                setState(data)
                drawState()
            }
        });
    }

    function retrieveGrid(){
        websocket.send("retrieveGrid")
    }
    function setGridData(data){
        let gridStr = data.substring(data.indexOf('GRID:')+5)
        gridXCount = parseInt(gridStr.split(',')[0]);
        gridYCount = parseInt(gridStr.split(',')[1]);
        offsetX = canvas.width / gridXCount
        offsetY = canvas.height / gridYCount

    }
    function drawGrid(){
        for ( i = 0 ; i < gridXCount ; i ++){
            ctx.moveTo(offsetX*(i+1),0);
            ctx.lineTo(offsetX*(i+1),canvas.height)
            ctx.stroke()
        }
        for ( i = 0 ; i < gridYCount ; i ++){
            ctx.moveTo(0, offsetY*(i+1));
            ctx.lineTo(canvas.width, offsetY*(i+1))
            ctx.stroke()
        }
    }

    function setState(data){
        let stateStr = data.substring(data.indexOf('STATE:')+6)
        x = parseInt(stateStr.split(",")[0]);
        y = parseInt(stateStr.split(",")[1]);
        f = stateStr.split(",")[2];

    }

    function drawState(data){

        ctx.clearRect(0,0,canvas.width, canvas.height)
        drawGrid()
        let xPos = x * offsetX;
        let yPos = canvas.height-((y+1)*offsetY);
        let img;
        if (f == 'NORTH'){
            img = arrowNorth
        }
        if(f == 'SOUTH'){
            img = arrowSouth
        }
        if( f == 'EAST'){
            img = arrowEast
        }
        if(f == 'WEST'){
            img = arrowWest
        }

        ctx.drawImage(img, xPos, yPos , offsetX, offsetY);
    }
})()
