$(function(){
    let s_count = 1;

    // json 불러오기
    $.ajax({
        url:"http://127.0.0.1:5500/students/json/stu_score.json",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            //alert("불러오기 성공")
            s_count = data.length;
            let h_data = "";
            for(let i=0;i<10;i++){
                h_data += "<tr id='"+data[i].no+"'>";
                h_data += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'</td>";
                h_data += "<td>"+data[i].no+"</td>";
                h_data += "<td>"+data[i].name+"</td>";
                h_data += "<td>"+data[i].kor+"</td>";
                h_data += "<td>"+data[i].eng+"</td>";
                h_data += "<td>"+data[i].math+"</td>";
                h_data += "<td>"+data[i].total+"</td>";
                h_data += "<td>"+data[i].avg+"</td>";
                h_data += "<td>"+data[i].rank+"</td>";
                h_data += "<td><button class='delBtn'>삭제</button></td>";
                h_data += "</tr>";
            }
            $("#body").html(h_data);
        },
        error:function(){
            alert("불러오기 실패");
        }
    }); // ajax

    // 학생입력
    $("#writeBtn").click(function(){
        $(".p_all").css("display","block");
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);
    }); // writeBtn
    
    $("#cancelBtn").click(function(){
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");
    });// cancelBtn

    $("#confirmBtn").click(function(){
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(2);
        s_count += 1


        let h_data = "";
            h_data += "<tr id='"+s_count+"'>";
            h_data += "<td><input type='checkbox' name='stu' class='stuChk' value='"+s_count+"'</td>";
            h_data += "<td>"+s_count+"</td>";
            h_data += "<td>"+i_name+"</td>";
            h_data += "<td>"+i_kor+"</td>";
            h_data += "<td>"+i_eng+"</td>";
            h_data += "<td>"+i_math+"</td>";
            h_data += "<td>"+i_total+"</td>";
            h_data += "<td>"+i_avg+"</td>";
            h_data += "<td>0</td>";
            h_data += "<td><button class='delBtn'>삭제</button></td>";
            h_data += "</tr>";
        $("#body").append(h_data);

        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");
    }); // confirmBtn

    // 학생 전체 선택, 해제
    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){ // 모든 개인 체크박스를 찾음
                $(this).prop("checked",true);
            });
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
        }
    });


    // 학생 삭제(테이블 내)
    $(document).on("click",".delBtn",function(){
        if(confirm("정말로 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    }); // delBtn

    // 학생 삭제(하단버튼)
    $("#deleteBtn").click(function(){
        $(".stuChk").each(function(){
            if($(this).is(":checked")==true){
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        });
    }); // deleteBtn

    // 학생 수정
    $("#modiftBtn").click(function(){
        
        $("#body").append(h_data);
    });// modifyBtn
}); // jquery