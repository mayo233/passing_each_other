//import gab.opencv.*;

PImage given_img;    //初期地図
PImage block_img = createImage(width, height, RGB);
PImage change_right_img_1 = createImage(width, height, RGB);

//変数宣言 エージェント
int N=3;  //エージェントの数
int[] agent_start ={100, 200, 450};  //100 200 450
int[] agent_goal ={490, 20, 70};   //490 20 70
int[][] agent =new int[N][2]; //エージェントN台 x,y座標を所有
int agent_x =10;    //agentのx座標の大きさ
int agent_y =10;   //agentのy座標の大きさ
int agent_num=-1;  //空きスペースに入るエージェント番号
int change_right_time; //エージェントの停止時間
int count_collision;  //衝突回数
int space_enter_t=0;    //ブロックを壊し始める時間
int step=0;  //ステップ数を計測
int count =0;
int B=66; //ブロックの個数
int break_block_num_num=0;  //改変するブロック番号
int change_right_agent;
//ブロックの変数宣言
int[] blf =new int[B] ; //ブロックの数
int blw =10;    //ブロックの横幅
int blh =10;  //ブロックの縦幅
int break_block_num=0;  //破壊するブロック

//判定を行う変数宣言
boolean collision ; //エージェント同士が衝突しそうになったか判定する変数
boolean space ; //空きスペースに入るのか判定する変数
boolean once =false;    //どっちのエージェントが空きスペースに入るか判定する
boolean second =false;    //どっちのエージェントが空きスペースに入るか判定する

boolean change_right =false;  //エージェントを停止させるか判定する
boolean change_left =false;  //エージェントを停止させるか判定する
boolean display =false;  //エージェントを停止させるか判定する
boolean block_num=false;  //エージェントを停止させるか判定する

////ブロックとエージェントの当たり判定
int blockHitCheck(int num) {

  //if (agent_num ==0 || agent_num ==1) {
  //  if (block_num ==false) {
  //    break_block_num =agent[2][0]/12;
  //    block_num=true;
  //  }
  //}
  //println(break_block_num_num);

  break_block_num =agent[num][0]/12;
  //println(break_block_num);
  //if (break_block_num <0){
  //  break_block_num
  //}


  return abs(break_block_num);
}

//衝突したエージェントのどっちが空きスペースに入るか判定する関数
int agent_or_space () {
  if (((agent[0][0]) -((agent[0][0]/12) *12) + blw/2) < ((agent[1][0] ) - ((agent[1][0]/12) *12) + blw/2 )) {
    return 0;
  } else if (((agent[0][0]) -((agent[2][0]/12) *12) + blw/2) < ((agent[0][0] ) - ((agent[2][0]/12) *12) + blw/2 )) {

    return 1;
  } else {
    return 2;
  }
}

void move_chnage(int num) {
  if (collision ==false) {
    for (int i=0; i<N; i++) {
      if ((num==i  && (agent_goal[i] - agent_start[i]) >0)  ) {
        //println(i);
        change_right=true;   //右から左に進む
      } else {
        change_left =false;    //左から右に進む
      }

      if ((agent_goal[i] - agent_start[i]) >0 ) {
        if (change_right==false ) {
          agent[i][0] +=1;
          println(abs(break_block_num));
          if (agent[i][0]==512){
            given_img.set(((abs(break_block_num )%B)) *(blw+2), 80, block_img);
            given_img.save("change_map.png");
            exit();
          }
        } else {
          agent[i][0] -=1;
          if (agent[N-1][0] ==-15 ) {
            display=true;
          }
        }
      } else {
        if (change_left==false ) {
          agent[i][0] -=1;
        } else {
          agent[i][0] +=1;
        }
      }
      if (display==true) {
        //agent[0][0] +=1;
        change_right=false;
        change_left=false;
      }
    }
  }
}

void agent_move() {
  move_chnage(-1);   //エージェントの方向を切り替える関数

  //衝突しそうになったら
  if ((agent[0][0] - agent[1][0] <=30 )  && (agent[0][0] - agent[1][0] >=-30 )) {
    if (once ==false) {
      agent_num=agent_or_space();
      move_chnage(agent_num);
      //change_right=true;
      break_block_num_num=blockHitCheck(agent_num);
      once =true;
    }
  } else if ((agent[0][0] - agent[2][0] <=30 )  && (agent[0][0] - agent[2][0] >=-30)) {
    if (once ==true && second ==false) {
      agent_num=agent_or_space();
      break_block_num_num=blockHitCheck(agent_num);
      second =true;
    }
  }

  for (int i =0; i<N; i++) {
    //エージェント番号を可視化
    textSize(40);
    if (i==0) {
      text( "1", agent[i][0], agent[i][1] +20, 60, 600);
    } else if (i==1) {
      text( "2", agent[i][0], agent[i][1] +20, 60, 600);
    } else {
      text( "3", agent[i][0], agent[i][1] +20, 60, 600);
    }
    ellipse(agent[i][0], agent[i][1], agent_x, agent_y);  //エージェントを表示させる
  }
  //step+=1;
  //println(step);
}
void setup() {
  size(500, 500);
  given_img=loadImage("given_map.png");
  block_img=loadImage("black_block.png");

  //初期設定
  size( 500, 500);
  agent[0][0] =100; //agent[0]のx座標の初期位置
  agent[0][1] =100; //agent[0]のy座標の初期位置
  agent[2][0] =400; //agent[2]のx座標の初期位置
  agent[2][1] =100; //agent[2]のy座標の初期位置
  count_collision =0; //衝突回数
  change_right_time=0;
  collision =false; //衝突していない
  space =false; //空きスペースに入っていない
  step=0; //ステップ数を計測

  //各エージェントに初期位置を代入
  for (int i =0; i<N; i++) {
    agent[i][0] =agent_start[i];
    agent[i][1] =100;
  }
}

void draw() {
  image(given_img, 0, 0);    //初期地図を表示
  agent_move();  //エージェントを動かす
}
