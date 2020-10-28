<template>
   <div id="Content">
   <el-container style="height: 800px; border: 1px solid #eee">
     <el-aside width="250px" style="background-color: rgb(238, 241, 246)">
       <el-menu :default-openeds="['1', '9']">
         <el-submenu index="1"  @click.native="num=1">
           <template slot="title"><i class="el-icon-menu"></i>检测站分布图</template>
           <el-menu-item-group>
             <template slot="title" >展示该地区水质地图</template>
           </el-menu-item-group>
         </el-submenu>
         <el-submenu index="2" >
           <template slot="title"><i class="el-icon-menu" ></i>数据预处理</template>
           <el-menu-item-group>
             <template slot="title">功能介绍</template>
             <el-menu-item index="2-1" @click="num=2">Show Me</el-menu-item>
             <el-menu-item index="2-2">数据集1配置路径</el-menu-item>
             <el-menu-item index="2-3">数据集2配置路径</el-menu-item>
           </el-menu-item-group>

         </el-submenu>
         <el-submenu index="3" @click.native="num=3">
           <template slot="title"><i class="el-icon-menu"></i>关联分析</template>
           <el-menu-item-group>
             <template slot="title">功能介绍</template>
             <el-menu-item index="3-1">配置数据集路径</el-menu-item>
           </el-menu-item-group>
         </el-submenu>

         <el-submenu index="4" @click.native="num=4">
           <template slot="title"><i class="el-icon-menu"></i>回归分析</template>
           <el-menu-item-group>
             <template slot="title">功能介绍</template>
             <el-menu-item index="4-1">配置数据集路径</el-menu-item>
           </el-menu-item-group>
         </el-submenu>
         <el-submenu index="5" @click.native="num=5">
           <template slot="title"><i class="el-icon-menu"></i>聚类分析</template>
           <el-menu-item-group>
             <template slot="title">功能介绍</template>
             <el-menu-item index="5-1">配置数据集路径</el-menu-item>
             <el-menu-item index="5-2">选择聚类个数</el-menu-item>
             <el-menu-item index="5-3">修改最大迭代次数</el-menu-item>
             <el-menu-item index="5-4">修改初始化质心次数</el-menu-item>
           </el-menu-item-group>
         </el-submenu>

         <el-submenu index="6" @click.native="num=6">
           <template slot="title"><i class="el-icon-menu"></i>时间序列分析</template>
            <el-menu-item-group>
             <template slot="title">功能介绍</template>
               <el-menu-item index="6-1">配置数据集路径</el-menu-item>
          </el-menu-item-group>
         </el-submenu>

          <el-submenu index="7" @click.native="num=7">
               <template slot="title"><i class="el-icon-menu"></i>离散点检测</template>
                 <el-menu-item-group>
                 <template slot="title">功能介绍</template>
                   <el-menu-item index="7-1">配置数据集路径</el-menu-item>
                  </el-menu-item-group>
          </el-submenu>

          <el-submenu index="8" @click.native="num=8">
                 <template slot="title"><i class="el-icon-menu"></i>时间序列检测</template>
                <el-menu-item-group>
                  <template slot="title">功能介绍</template>
                   <el-menu-item index="8-1">配置数据集路径</el-menu-item>
                    </el-menu-item-group>
           </el-submenu>
           <el-submenu index="9" @click.native="num=9">
               <template slot="title"><i class="el-icon-menu"></i>异常点关联分析</template>
                 <el-menu-item-group>
               <template slot="title">功能介绍</template>
                <el-menu-item index="9-1">配置数据集路径</el-menu-item>
                 </el-menu-item-group>
            </el-submenu>
       </el-menu>
     </el-aside>

     <el-container>
       <el-header style="text-align: right; font-size: 12px">
       <el-page-header  content="详情页面" style="margin-top:20px">
       </el-page-header>
       <span>查看<i class="el-icon-view el-icon--right"></i> </span>
       <div class="demo-basic--circle"></div>
         <el-dropdown>
           <i class="el-icon-setting" style="margin-right: 15px"></i>
           <el-dropdown-menu slot="dropdown">
             <el-dropdown-item>查看</el-dropdown-item>
             <el-dropdown-item>新增</el-dropdown-item>
             <el-dropdown-item>删除</el-dropdown-item>
           </el-dropdown-menu>
         </el-dropdown>
         <span>游客</span>
       </el-header>

       <el-main>
         <div class='one' v-show="num==1">
          <el-card :body-style="{ padding: '0px' }" >
            <div style="padding: 14px;">
              <span>芗城水质</span>
               <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
               </div>
             </div>
            <img src="../assets/image1.png" class="image">
            </el-card>
         </div>

         <div class="two" v-show="num==2">
           <el-card class="box-card">
             <div slot="header" class="clearfix">
               <span>卡片展示</span>
                <i class="el-icon-loading" style="float: right"></i>
             </div>
             预处理数据集1<el-input v-model="input" placeholder="数据路径xxxxxxxxxx" :disabled="true">预处理数据集</el-input>
             预处理数据集2<el-input v-model="input" placeholder="数据路径xxxxxxxxxx" :disabled="true">预处理数据集2</el-input>
              <el-button style="margin-top: 12px;" @click="next"  >确认无误</el-button>
              <el-button style="margin-top:12px;margin-right:30px; float:right; border:1px solid black;" type="text" @click="dialogVisible = true">
              开始预处理数据</el-button>
              <el-dialog
                title="提示"
                :visible.sync="dialogVisible"
                width="40%"
                :before-close="handleClose">
                <span style="margin-left:300px;"><el-progress type="circle" :percentage="0"></el-progress></span>
              </el-dialog>
              <el-divider></el-divider>
              <el-card class="box-card1">
              图表展示区
              </el-card>
              <el-card class="box-card2">
              数据处理
               </el-card>
           </el-card>
          </div>

          <div class="three" v-show="num==3">
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>卡片展示</span>
                <i class="el-icon-loading" style="float: right"></i>
              </div>
              数据集<el-input v-model="input" placeholder="数据路径xxxxxxxxxx" :disabled="true">数据集</el-input>
              <el-steps :active="active" finish-status="success" style="margin-top:40px">
                <el-step title="步骤 1"></el-step>
                <el-step title="步骤 2"></el-step>
              </el-steps>
               <el-button style="margin-top: 12px;" @click="next">确认无误</el-button>
               <el-button style="margin-top:12px;margin-right:30px; float:right;" @click="next">使用apriori算法进行关联分析</el-button>
               <el-divider></el-divider>
               <el-card class="box-card1">
               结果分析
               </el-card>
               <el-card class="box-card2">
               共总耗时
                </el-card>
            </el-card>
           </div>

          <div class="four" v-show="num==4">
             <el-card class="box-card">
               <div slot="header" class="clearfix">
                 <span>卡片展示</span>
                 <i class="el-icon-loading" style="float: right"></i>
               </div>
               数据集<el-input v-model="input" placeholder="数据路径xxxxxxxxxx" :disabled="true">数据集</el-input>
               <el-steps :active="active" finish-status="success" style="margin-top:40px">
                 <el-step title="步骤 1"></el-step>
                 <el-step title="步骤 2"></el-step>
               </el-steps>
                <el-button style="margin-top: 12px;" @click="next">确认无误</el-button>
                <el-button style="margin-top:12px; margin-right:30px; float:right;" @click="next">开始多元回归分析</el-button>
                <el-divider></el-divider>
                <el-card class="box-card1">
                结果分析
                </el-card>
                <el-card class="box-card2">
                共总耗时
                 </el-card>
             </el-card>
            </div>

            <div class="fifth" v-show="num==5">
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>卡片展示</span>
                  <i class="el-icon-loading" style="float: right"></i>
                </div>
                数据集<el-input v-model="input" placeholder="数据路径xxxxxxxxxx"
                :disabled="true">数据集</el-input>
                 <span style="margin-left:20px;">聚类个数： <el-input-number v-model="num_a" @change="handleChange"  label="描述文字1"></el-input-number></span>
                 <span style="margin-left:100px;">最大迭代次数：<el-input-number v-model="num_b" @change="handleChange" label="描述文字2"></el-input-number></span>
                 <span style="margin-left:100px;">初始化质心个数：<el-input-number v-model="num_c" @change="handleChange"  label="描述文字3"></el-input-number></span>
                <el-steps :active="active" finish-status="success" style="margin-top:40px">
                  <el-step title="步骤 1"></el-step>
                  <el-step title="步骤 2"></el-step>
                  <el-step title="步骤 3"></el-step>
                </el-steps>
                 <el-button style="margin-top: 12px;" @click="next">确认无误</el-button>
                 <el-button style="margin-top:12px; margin-right:40px; float:right;" @click="next">使用Kmeans算法进行聚类分析</el-button>
                 <el-divider></el-divider>
                 <el-card class="box-card1">
                 结果分析
                 </el-card>
                 <el-card class="box-card2">
                 共总耗时
                  </el-card>
              </el-card>
             </div>
           <div class="six" v-show="num==6">
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>卡片展示</span>
                 <i class="el-icon-loading" style="float: right"></i>
              </div>
              数据集<el-input v-model="input" placeholder="数据路径xxxxxxxxxx" :disabled="true">数据集</el-input>
              <el-steps :active="active" finish-status="success" style="margin-top:40px">
                <el-step title="步骤 1"></el-step>
                <el-step title="步骤 2"></el-step>
              </el-steps>
               <el-button style="margin-top: 12px;" @click="next">确认无误</el-button>
               <el-button style="margin-top:12px;margin-right:30px; float:right; border:1px solid black;" type="text" @click="dialogVisible = true">
               开始时间序列分析</el-button>
               <el-dialog
                 title="提示"
                 :visible.sync="dialogVisible"
                 width="40%"
                 :before-close="handleClose">
                 <span style="margin-left:300px;"><el-progress type="circle" :percentage="0"></el-progress></span>
               </el-dialog>
               <el-divider></el-divider>
               <el-card class="box-card1">
               图表展示区
               </el-card>
               <el-card class="box-card2">
               数据处理
                </el-card>
            </el-card>
           </div>
           <!-- 离散点检测-->
         <div class="seven" v-show="num==7">
             <el-card class="box-card">
               <div slot="header" class="clearfix">
                 <span>卡片展示</span>
                 <i class="el-icon-loading" style="float: right"></i>
               </div>
               数据集<el-input v-model="input" placeholder="数据路径xxxxxxxxxx" :disabled="true">数据集</el-input>
               <el-steps :active="active" finish-status="success" style="margin-top:40px">
                 <el-step title="步骤 1"></el-step>
                 <el-step title="步骤 2"></el-step>
               </el-steps>
                <el-button style="margin-top: 12px;" @click="next">确认无误</el-button>
                <el-button style="margin-top:12px;margin-right:30px; float:right;" @click="next">开始离散点检测</el-button>
                <el-divider></el-divider>
                <el-card class="box-card1">
                结果分析
                </el-card>
                <el-card class="box-card2">
                共总耗时
                 </el-card>
             </el-card>
            </div>

           <!-- 时间序列检测-->
          <div class="eight" v-show="num==8">
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>卡片展示</span>
                  <i class="el-icon-loading" style="float: right"></i>
                </div>
                数据集<el-input v-model="input" placeholder="数据路径xxxxxxxxxx" :disabled="true">数据集</el-input>
                <el-steps :active="active" finish-status="success" style="margin-top:40px">
                  <el-step title="步骤 1"></el-step>
                  <el-step title="步骤 2"></el-step>
                </el-steps>
                 <el-button style="margin-top: 12px;" @click="next">确认无误</el-button>
                 <el-button style="margin-top:12px;margin-right:30px; float:right;" @click="next">开始时序检测</el-button>
                 <el-divider></el-divider>
                 <el-card class="box-card1">
                 平稳性，白噪声检测结果：
                 </el-card>
                 <el-card class="box-card2">
                  结果分析
                  </el-card>
              </el-card>
             </div>
          <!--异常点关联分析-->
          <div class="nine" v-show="num==9">
               <el-card class="box-card">
                 <div slot="header" class="clearfix">
                   <span>卡片展示</span>
                   <i class="el-icon-loading" style="float: right"></i>
                 </div>
                 数据集<el-input v-model="input" placeholder="数据路径xxxxxxxxxx" :disabled="true">数据集</el-input>
                 <el-steps :active="active" finish-status="success" style="margin-top:40px">
                   <el-step title="步骤 1"></el-step>
                   <el-step title="步骤 2"></el-step>
                 </el-steps>
                  <el-button style="margin-top: 12px;" @click="next">确认无误</el-button>
                  <div style="margin-top:20px">
                  <el-button :plain="true" @click="open2" >进行氨氮关联分析</el-button>
                  <el-button :plain="true" @click="open2" >进行电导率关联分析</el-button>
                  <el-button :plain="true" @click="open2" >进行高锰酸盐分析</el-button>
                  <el-button :plain="true" @click="open2" >进行浑浊度关联分析</el-button>
                  <el-button :plain="true" @click="open2" >进行溶解氧关联分析</el-button>
                  <el-button :plain="true" @click="open2" >进行总氮关联分析</el-button>
                  <el-button :plain="true" @click="open2" >进行总磷关联分析</el-button>
                  <el-button :plain="true" @click="open2" >进行ph异常值关联分析</el-button>
                  </div>

                  <el-divider></el-divider>
                  <el-card class="box-card1">
                  结果分析：
                  </el-card>
               </el-card>
              </div>
       </el-main>
     </el-container>
   </el-container>
   </div>
</template>

<script>
export default {
    data() {
      return {
        input:'',
        active: 1,
         dialogVisible: false,
        btn: 'ture',
        num: 1,
        num_a: 3,
        num_b: 300,
        num_c: 3,
        currentDate: new Date()
      }
    },
    methods: {
           open2() {
              this.$message({
              message: 'succeed！,开始分析',
              type: 'success'
             });
           },
          next() {
            if (this.active++ > 2)
            {
              this.active = 3;
              this.btn=false;
            }
          },
          handleChange(value) {
                  console.log(value);
          },
          text() {
                   console.log("1111111111");
          },
          handleClose(done) {
                  this.$confirm('确认关闭？')
                    .then(_ => {
                      done();
                    })
                    .catch(_ => {});
                }
          }
  }
</script>

<style>
.el-icon-loading {
  font-size: 25px;
}
   .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 12px;
  }

  .el-aside {
    color: #333;
  }
 .time {
     font-size: 13px;
     color: #999;
   }

   .bottom {
     margin-top: 13px;
     line-height: 12px;
   }

   .image {
     height:700px;
     width: 80%;
     display: block;
   }

   .clearfix:before,
   .clearfix:after {
       display: table;
       content: "";
   }

   .clearfix:after {
       clear: both;
   }
   .box-card {
        position:relative;
        height:950px;
          width: 100%;
        }
    .box-card1 {
    float:left;
       margin-left:80px;
       height:480px;
       width: 960px;
     }
     .box-card2 {
     float:right;
     margin-right:80px;
            height:480px;
            width: 400px;
     }
    .el-input-number {
       margin-top:30px;
    }
</style>
