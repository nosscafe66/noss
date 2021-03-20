
int screenWidth = 700;
int screenHeight = 700;

void settings() {
  size(screenWidth, screenHeight);
}

void draw(){

  
  int h = hour();
  int m = minute();
  int s = second();
  
  int a = 255-h;
  int b = 255-m;
  int c = 255-s;
  
  String t = h + ":" + nf(m, 2) + ":" + nf(s, 2);
  
  rect(0, 0, h*10, height/3); 
  rect(0, height/3, m*4, height/3);
  rect(0, height*2/3, s*4, height/3);
  


noStroke();
rect(0,0,269.23,269.23);
translate(350,-350);
rotate(PI/30);
if(a <240){
  fill(a,b,c,30);
      rect(0,0,269.23,269.23);
      rect(269.25,0,161.55,161.55);
      rect(0,269.25,430.77,430.77);
}
if(b < 230){
      fill(a,b,255,30);
      rect(323.08,161.55,107.7,107.7);
      translate(269.25,161.55);
      rect(0,0,53.85,53.85);
      translate(0,53.85);
      rect(0,0,53.85-s,53.85-s);
}
 

//line(430.8,0,430.8,700);
//fill(random(255),random(10),random(255),random(255));
rect(269.25,0,161.55,161.55);
translate(-350,350);
if(s == 2){
rotate(PI/60);
fill(30, 120, 255, 5);
      rect(0,0,269.23,269.23);
      rect(269.25,0,161.55,161.55);
      rect(0,269.25,430.77,430.77);
      fill(0,0,0,5);
      rect(323.08,161.55,107.7,107.7);
      translate(269.25,161.55);
      rect(0,0,53.85,53.85);
}
if(s > 5 || 10 >s){
      fill(255,128,0,5);
      translate(0,53.85);
      rect(0,0,53.85-s,53.85-s);
}
//line(0,269.25,430.8,269.25);
//fill(random(255),random(255),random(10),random(255));

if(s == 13){
rect(0,269.25,430.77,430.77); 
translate(-350,-350);
rotate(PI/90);
      
      rect(0,0,269.23,269.23);
      rect(269.25,0,161.55,161.55);
      rect(0,269.25,430.77,430.77);
      rect(323.08,161.55,107.7,107.7);
}
if(s == 60){
  fill(-30+s, 60+s, 255, 5);
      translate(269.25,161.55);
      rect(0,0,53.85,53.85);
      translate(0,53.85);
      rect(0,0,53.85,53.85);
}

//line(269.25,0,269.25,269.25);
if(s > 28 || 35 > s){
rect(323.08,161.55,107.7,107.7);
fill(60, 120, 255, 5);
translate(350,350);
rotate(PI/180);
      rect(0,0,269.23,269.23);
      rect(269.25,0,161.55,161.55);
}
      rect(0,269.25,430.77,430.77);
      rect(323.08,161.55,107.7,107.7);
      translate(269.25,161.55);
      rect(0,0,53.85,53.85);
      translate(0,53.85);
      rect(0,0,53.85,53.85);


//line(269.25,161.55,430.8,161.55);
translate(269.25,161.55);
//fill(random(10),random(255),random(255),random(255));
rect(0,0,53.85,53.85);
translate(0,53.85);
//fill(random(255),random(255),random(255),random(255));
rect(0,0,53.85,53.85);
rotate(PI);
      rect(0,0,269.23,269.23);
      rect(269.25,0,161.55,161.55);
      rect(0,269.25,430.77,430.77);
      rect(323.08,161.55,107.7,107.7);
      translate(269.25,161.55);
      rect(0,0,53.85,53.85);
      translate(0,53.85);
      rect(0,0,53.85,53.85);

}


/*
for(int i = 0; i < width; i++){
  int c = 255 * i / width;
  stroke(c);
  line(i, 0, i, height);
}

*/
