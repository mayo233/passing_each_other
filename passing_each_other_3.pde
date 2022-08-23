//エージェントの数をNにして　forでまわす そして

//変数宣言
int N =3;  //エージェントの数
int[] agent_start ={100, 300, 400};
int[] agent_goal ={490, 20, 70};
int agent_x =10;
int agent_y =10;
int[][] agent =new int[N][2]; //エージェントN台 x,y座標を所有
int before_2 =0;
int before_1 =0;


int[] blf =new int[50] ; //ブロックの数
int blw =10;
int blh =10;
int delete_b =0;
int before=0;
int agent_num=0;
int space_enter_t=0;
int space_enter_t2=0;


int count_collision_time =0;  //エージェント同士
boolean collision ; //衝突しそうになったか判定する変数
boolean space ; //空きスペースに入るのか判定する変数
boolean stop; //停止させるか判定する変数
boolean stop_1; //停止させるか判定する変数
boolean stop_2; //停止させるか判定する変数
boolean temp =false;
boolean once =false;
boolean second =false;

int block_count=0;
int stop_time; //停止時間
int count_collision;  //空きスペースに入って衝突回避を行った回数


void blockDisp() {
  for (int i=0; i<blf.length; i++) {
    blf[i] =1;  //0:ブロック非表示 1:ブロック表示
  }
  for (int i=blf.length-1; i >=0; i--) {

    if (blf[i] ==1) {
      fill(255, 255, 255);
      blockHitCheck();

      rect((i%50) *(blw+2), 80, blw, blh);    //上のブロック
    }
    rect((i%50) *(blw+2), 110, blw, blh);    //下のブロック
  }
}

//ブロックとエージェントの当たり判定 ブロックを消す
void blockHitCheck() {

  if ((agent[0][1] !=100) && count_collision ==0) {
    before =agent[0][0]/12;
  } else if (agent[2][1] ==90 ) {
    before_2 =agent[2][0]/12;
  } else if ((agent[0][1] !=100 && (count_collision ==1 || count_collision ==2)) ) {
    before_1 =agent[0][0]/12;
    println(before_1);
  }

  if (before !=0  || before_1!=0) {
    blf[before]=0;
  }

  if (before_1 !=0  ) {
    blf[before_1] =0;
  }


  if (before_2 !=0) {
    //println("２回目の衝突なのでブロックを壊します");
    blf[before_2] =0;
  }
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

void agent_move() {
  //agent[1][0] -=1;

  ////160 衝突 バックを入れる？？  123 うまくいった  128　微妙?
  //if (stop_time  >=123 && collision ==false) {
  //  agent[1][0] -=1;
  //  //stop_time=0;
  //}

  for (int i=0; i<N; i++) {

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
    for (int j =0; j<N; j++) {
      if (i ==j) {
        continue;
      }

      //エージェント同士が衝突しそうになった時
      if ((agent[0][0] - agent[1][0] <=30 )  && (agent[0][0] - agent[1][0] >=-30 ) || (agent[0][0] - agent[2][0] <=30 )  && (agent[0][0] - agent[2][0] >=-30 )) {
        //println("衝突する");
        //println(second);
        //if ((agent[0][0] - agent[2][0] <=30 )  && (agent[0][0] - agent[2][0] >=-30)){
        //  println(agent[0][0] -agent[2][0]);
        //  noLoop();
        //}


        //println(i);
        //println(j);
        //println(agent[0][0] - agent[2][0] );

        if (once ==false) {
          agent_num = agent_or_space();
          once =true;
        }

        if (second ==false  && once ==true  && (agent[0][0] -agent[2][0] <=30 && agent[0][0] -agent[2][0] >=-30)) {
          agent_num = agent_or_space();


          second =true;
        }

        if (count_collision ==0  || (once ==true && second ==true)) {
          collision =true;
        }
      }
    }
  }

  //衝突しそうにない時，各エージェントは指定されたゴール地点に向かう
  if (collision ==false ) {
    for (int i=0; i<agent.length; i++) {
      if ((agent_goal[i] - agent_start[i]) >0) {
        agent[i][0] +=1;
      } else {
        agent[i][0] -=1;
      }
    }
  } else if (collision ==true) {
    if (space ==false) {
      //衝突しそうになっていて空きスペースに入っていない時
      //println("衝突しそうになっていて空きスペースに入っていない");
      //println(agent[0][0]);

      if (agent_num ==0) {

        agent[0][1] -=1;
        agent[1][0] -=1;
        agent[2][0] -=1;
      } else if (agent_num ==1) {
        agent[0][0] +=1;
        agent[1][1] -=1;
        agent[2][0] -=1;
        //noLoop();
      } else {
        //println(agent_num);
        agent[0][0] +=1;
        agent[1][0] -=1;
        agent[2][1] -=1;
        //println("えーじぇんと3");
        //println(agent[2][1]);
      }
      if (agent[0][1] ==85 || agent[1][1] ==85  || agent[2][1] ==85) {
        //println(agent[0][1]);
        //println(agent[1][1]);
        //println(agent[2][1]);
        //println("------");

        space =true;
        //println("エージェント３は秋から出る");
        if (agent_num ==0) {
          agent[0][0] +=1;
          agent[1][1] -=1;
          agent[2][1] -=1;
        } else if (agent_num ==1) {
          agent[0][1] +=1;
          agent[1][0] +=1;
          agent[2][0] -=1;
        } else {
          agent[0][0] -=1;
          agent[1][0] +=1;
          agent[2][1] +=1;
        }
      }
    } else if (space ==true) {

      //ブロックを壊した時
      if (agent_num ==0) {
        if (stop ==false && count_collision ==0) {
          space_enter_t =millis()/1000;
          stop=true;
        } else if (stop==true && count_collision ==1) {
          space_enter_t =millis()/1000;
          stop=false;
        }

        if ((millis()/1000- space_enter_t)==1 && agent[0][1] !=100) {
          agent[0][1] +=1;
        }


        agent[1][0] -=1;
        agent[2][0] -=1;
      } else if (agent_num ==1) {
        agent[0][0] +=1;
        agent[1][1] +=1;
        agent[2][0] +=1;
      } else {
        if (stop_2 ==false) {
          println("現在時間");
          space_enter_t =millis()/1000;

          stop_2=true;
        }

        if ((millis()/1000- space_enter_t )==2 && count_collision ==1) {

          agent[2][1] +=1;
        }
        //if (agent[2][1]  !=100) {
        //  println("出来てる");
        //  agent[2][1] +=1;
        //}
        agent[0][0] +=1;
        agent[1][0] -=1;
      }

      if (((agent[0][1] ==100 ) && (collision ==true && space ==true ) )  || (agent[0][1] ==100 && second ==true) ) {
        if (second ==false) {
          collision =false;
          space =false;
          count_collision++;
        } else {
          println("終わったの？");
          collision =false;
          println(agent[0][0]);

          //agent[0][0] +=1;
        }
      }
    }
  }
  stop_time+=1;    //停止時間
}

void setup() {
  //初期設定
  size(500, 500);
  count_collision_time =0; //衝突回数時間
  count_collision =0; //衝突回数
  stop_time=0;
  before=0;
  collision =false; //衝突していない
  space =false; //空きスペースに入っていない
  stop =false;
  stop_1 =false;
  stop_2 =false;


  //各エージェントに初期位置を代入
  for (int i =0; i<N; i++) {
    agent[i][0] =agent_start[i];
    agent[i][1] =100;
  }
}

void draw() {

  background(0); //背景を黒にする
  blockDisp();    //ブロックの表示
  agent_move();  //エージェントを動かす
}
