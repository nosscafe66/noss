//今編集しているプログラム
float VEL = 100.0;//最大加速
float ACC = 2.5;//最大加速度
ArrayList<Particle> particles;
ArrayList<Particle> particles2;
ArrayList<Particle> particles3;
PVector l = new PVector();
float x = random(0, width); 
float y = random(0, height); 
float speedX = 5; 
float speedY = 4; 
int time1 = 2500;
int time2 = 5000;
int time3 = 7500;
int time4 = 10000;
int time5 = 12500;
int time6 = 15000;
int time7 = 17500;
int h = 0 ;
int s = 100;
int b = 100;

import ddf.minim.*;
Minim minim;
AudioPlayer player;

void setup(){
  size(980, 730, P3D);

  particles3 = new ArrayList<Particle>();  
  for(int i = 0; i < 2000; i++){
    particles3.add(new Particle());

  }
  
  minim = new Minim(this);
  player = minim.loadFile("Eternal Garden - Dan Henig.mp3");
  player.loop();
  
smooth(4);
}


void draw(){
  background(250,250,250,5);
  lights();
  translate(width/2, height/2,0);
  rotateX(-PI/4);
  rotateY(frameCount*0.01);
  rotateZ(PI/4);
  //l.set( mouseX, mouseY, 0 );
  //translate(width/2,height/2, 0);
  /*
  for(Particle p: particles){
    //rotateX(frameCount);
    //rotateY(frameCount*0.001);
    //rotateZ(frameCount);
    p.display4();
    p.update3();
  }
  
  for(Particle p: particles2){
    //rotateX(frameCount*0.001);
    //rotateY(frameCount);
    //rotateZ(frameCount);
    p.display4();
    p.update3();
  }
  */
  
  for(Particle p: particles3){
    //rotateX(frameCount*0.001);
    //rotateY(frameCount*0.001);
    //rotateZ(frameCount*0.001);
    int time = millis();


       
       
if (time > time1) {
p.display4();
p.update3();
}
if (time > time2) {
p.stop();
}
if (time > time3) {
//loop();
p.display4();
p.update2();
}
if (time > time4) {
p.display4();
p.update2();
}
if (time > time5) {
p.display3();
p.update3();
}
if (time > time6) {
p.stop();



}
if (time > time7) {

p.update3();
p.display4();
}

  /*
  saveFrame("frames/####.png");
if (frameCount >= 4500) {
  exit();
 }
 */
 //rec();
 //saveFrame("frames/####.png");
}

}


class Particle{
  
  PVector pos, vel, acc,gravity,loc,sp,force;
 

  
  Particle(){
    
    float posSize = random(800,800);
    float posAng1 = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float posAng2 = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));//map(sin(frameCount*0.01), -100, 100, 0, -100)
    float posX = posSize * sin(posAng1) * posAng2;
    float posY = posSize * posAng1 * posAng2; 
    float posZ = posSize * posAng1;
    pos = new PVector(posX, posY, posZ);
    float velSize = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));
    float velAng1 = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float velAng2 = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float velX = velSize * velAng1 * velAng1;
    float velY = velSize * velAng1 * velAng2;
    float velZ = velSize * velAng1;
force = new PVector(12.0, 8.0);
vel = new PVector(velX,velY,velZ);
loc = new PVector(random(0, width ), random( 0, height ), random( -100, 100 ));//random(-width, width ), random( -height, height ), random( -100, -700 )
pos = new PVector(random(0,width), random(0,height), random(-100, 100));
sp = new PVector();
acc = new PVector();
gravity  = new PVector(0.005,0.005,0.005);//0.5,0.5,0.5
acc = force.mult(ACC);
    
    
    

  } 
  
  
  
  
  
  void update1(){
  
    //if(mousePressed){
      float mix = player.left.level() * width/100;
      PVector dir = new PVector(mouseX,mouseY, 100);//random(map(sin(frameCount*0.01), -1, 1, 0, -1000))
      dir.sub(pos);
      dir.normalize();
      sp.add(dir);
      //acc.limit(ACC*mix);
      vel.add(acc);
      //dir.add(acc,acc,acc);
      vel.limit(VEL*mix);
      pos.add(sp);
      vel.add(gravity);
      //dir.dist(acc,acc);
  //}
   // else
  // {
   //   vel.mult(.9);
   // }
    pos.add(sp);
    
    //PVector mouse = new PVector(map(mouseX, 0, width, -width / 2, width / 2), map(mouseY, 0, height, -height / 2, height / 2), 100);//map(mouseX, 0, width, -width / 2, width / 2), map(mouseY, 0, height, -height / 2, height / 2), 500
    //PVector acc = PVector.sub(mouse, pos);
    
  }
  
  void update2(){
  
   // if(mousePressed){
      float mix = player.left.level() * width/100;
      PVector dir = new PVector(mouseX,mouseY, -100);//random(map(sin(frameCount*0.01), -1, 1, 0, -1000))
      dir.sub(pos);
      dir.normalize();
      sp.add(dir);
      //acc.limit(ACC*mix); ---
      vel.add(acc);
      //dir.add(acc,acc,acc);
      vel.limit(VEL*mix);
      //pos.add(sp); --
      vel.add(gravity);
      //dir.dist(acc,acc);
  //}
  //  else
  // {
   //   vel.mult(.9);
   // }
    pos.add(sp);
    
    //PVector mouse = new PVector(map(mouseX, 0, width, -width / 2, width / 2), map(mouseY, 0, height, -height / 2, height / 2), 100);//map(mouseX, 0, width, -width / 2, width / 2), map(mouseY, 0, height, -height / 2, height / 2), 500
    //PVector acc = PVector.sub(mouse, pos);
    
  }
  
  void update3(){
   // if( mousePressed )
    //{

      float mix = player.left.level() * width/100;
    
      PVector dir = new PVector(vel.x,vel.y,vel.z);//random(map(sin(frameCount*0.01), -1, 1, 0, -1000))
      
      dir.sub(pos);
      dir.normalize();
      
      acc.set(sp.x,sp.y,sp.z);
      sp.add(dir);
      acc.limit(ACC*mix);
      vel.add(acc);
      //dir.add(acc,acc,acc);
      vel.limit(VEL*mix);
      pos.add(sp);
      vel.add(gravity);
      


   // }
   // else
   //{
   //   vel.mult(.9);
   // }
    pos.add(sp);//posと同じ speedはvelと同じ
  }
  
  void update(){
    int inc = 2;
    float mix = player.left.level() * width/100;
 // if( mousePressed )
  //  {
      PVector dir = new PVector( mouseX, mouseY, -500 );
      dir.sub( pos );
      dir.normalize();
      sp.add( dir );
      pos.add( sp );//posと同じ speedはvelと同じ　　
   
  }
  
  void stop(){
      //sp = new PVector();
      //loc = new PVector(random(0, width ), random( 0, height ), random( -100, -700 ));

      sp.mult( .1 );
      sp.add(gravity);
      //acc.add(sp.x,sp.y,sp.z);
      //acc = force.mult(ACC);
      sp.add(acc);
  }
  
  
 

  
  void display1(){
 
    float mix = player.left.level() * width/50;
    pushMatrix();
    rotateToFace(pos);//240,200,220,5
    translate(-pos.x, pos.y, -pos.z);
    fill(50,200,250,100);
    ellipse(pos.x+mix, pos.y+mix, ACC, ACC);
    translate(pos.x, pos.y, pos.z);
    fill(250,200,200,200);
    ellipse(-pos.x+mix, -pos.y+mix, ACC, ACC);
    translate(loc.x, -loc.y, loc.z);
    fill(250,250,250,200);
    ellipse(-pos.x+mix, -pos.y+mix, ACC, ACC);
    popMatrix();
  }
  void display2(){
    float mix = player.left.level() * width/100;
    pushMatrix();
    rotateToFace(pos);
    translate(-pos.x, pos.y, -pos.z);
    fill(240+pos.x,0+pos.y,0+pos.z,100);
    ellipse(pos.x+mix, pos.y, ACC, ACC);
    //ellipse(random(ACC), random(ACC), ACC, ACC); 
    popMatrix();
  }
  
  void display3(){
    float mix = player.left.level() * width/200;
    pushMatrix();
    rotateToFace(pos);
    translate(-pos.x, pos.y, -pos.z);
    //fill(250-pos.x,150-pos.y,100-pos.z,100);
    stroke(250+pos.x,20,20,250);
    fill(250+pos.x,20,20,250);
    ellipse(pos.x+mix, pos.y, ACC, ACC);
    //ellipse(random(ACC), random(ACC), ACC, ACC); 
    popMatrix();
  }
  
  
  void display4(){
  int time = millis();
  float mix = player.left.level() * width/200;


    pushMatrix();
    rotateToFace(pos);
    //translate(-pos.x, -pos.y, -pos.z);
    //fill(250-pos.x,150-pos.y,100-pos.z,100);
    //colorMode(RGB, 360, s, b);
    //fill(h, 199, 199,255); 
    fill(0,0,0,250);
    stroke(0,0,0,250);
    //stroke(h+pos.x, 199, 199,200);
    ellipse(pos.x, -pos.y, ACC, ACC);
    //ellipse(random(ACC), random(ACC), ACC, ACC); 
    popMatrix();
 x += speedX; 
 y += speedY; 
 
 if (x < 0 || x > width) { 
   speedX *= -1;
 } 
 if (y < 0 || y > height) { 
   speedY *= -1;
 }

 if (time > time1) {
   h = 30;
 }
 if (time > time2) {
   h = 60;
 }
 if (time > time3) {
   h = 120;
 }
 if (time > time4) {
   h = 180;
 }
 if (time > time5) {
   h = 240;
 }
 if (time > time6) {
   h = 270;
 }
 if (time > time7) {
   h = 0;
 }

  
  
  
  }
  
  
  
PVector U = new PVector(100,100,100); //1000, 1000, 1000 
void rotateToFace( PVector P )
{
  PVector D = new PVector();//1000, 1000, 1000
  D.set(l);
  D.sub(P);
  PVector r = U.cross( D );

  r.normalize();
  PVector Backwards = r.cross( U );

  Backwards.normalize();
  PVector rUp = Backwards.cross(r);

  applyMatrix(r.z, r.x, r.y, 0, rUp.x, rUp.y, rUp.z, 0, Backwards.x, Backwards.y, Backwards.z, 0, 0, 0, 0, 1);
}


  
  }
  
  
  
  
  
  /*
  float posSize = random(800,800);
    float posAng1 = random(map(sin(radians(TWO_PI)), -1, 1, 200, 300));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float posAng2 = random(map(sin(radians(-TWO_PI)), -1, 1, 100, 200));//map(sin(frameCount*0.01), -100, 100, 0, -100)
    float posX = posSize * sin(posAng1) * posAng2;
    float posY = posSize * posAng1 * posAng2; 
    float posZ = posSize * posAng1;
    pos = new PVector(posX, posY, posZ);
    float velSize = random(map(-sin(radians(800)), -1, 1, 200, 100));
    float velAng1 = random(map(-sin(radians(-TWO_PI)), -1, 1, 200, 300));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float velAng2 = random(map(sin(radians(TWO_PI)), -1, 1, 30, 600));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float velX = velSize * velAng1 * velAng1;
    float velY = velSize * velAng1 * velAng2;
    float velZ = velSize * velAng1;
  
  
  */
