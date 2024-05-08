$(function(){

    // 최초 실행 --------------------------------------------------------------------------
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [76,91,81,99,61,82,63,80,64,55];
    let eng = [60,75,58,56,96,85,59,58,98,65];
    let math = [73,88,56,61,77,69,76,65,68,81];
    let total = [209,254,195,216,234,236,198,203,230,201];
    let avg = [69.6,84.6,65,72.6,78,78.7,66,67,76.6,67];

    let htmlData = "";
    for(let i=0;i<no.length;i++){ 

        htmlData += "<tr id="+(i+1)+">";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value="+(i+1)+"></td>";
        htmlData += "<td>"+no[i]+"</td><td>"+name[i]+"</td>";
        htmlData += "<td>"+kor[i]+"</td><td>"+eng[i]+"</td><td>"+math[i]+"</td>";
        htmlData += "<td>"+total[i]+"</td><td>"+avg[i]+"</td><td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
    };

    $("#body").html(htmlData); // tbody에 행 추가
//--------------------------------------------------------------------------최초 실행

    // 학생입력버튼 클릭
    $("#writeBtn").click(function(){
        $(".p_all").css("display","block");
    });
    
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
    });

    // 학생입력확인 버튼
    $("#confirmBtn").click(function(){
        console.log("이름 : "+$("#name").val());
        // 공백 확인
        if($("#name").val().length<2){
            alert('이름을 다시 입력하세요');
            $("#name").focus();
            return false;
        }

        console.log("국어 : "+$("#kor").val());
        console.log("영어 : "+$("#eng").val());
        console.log("수학 : "+$("#math").val());
        // console.log(Math.max.apply(null,no)+1); // 배열에서 최대값 구하기
        //no.push(Math.max.apply(null,no)+1); // push 배열에 추가
        let i_no = Math.max.apply(null,no)+1;
        no.push(i_no);
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(2); // 함수 자르기 (소수점 2자리 반올림)
        let i_rank = 0;

        // table tr에 추가
        let htmlData = "";
        htmlData += "<tr id="+i_no+">";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value="+i_no+"></td>";
        htmlData += "<td>"+i_no+"</td><td>"+i_name+"</td>";
        htmlData += "<td>"+i_kor+"</td><td>"+i_eng+"</td><td>"+i_math+"</td>";
        htmlData += "<td>"+i_total+"</td><td>"+i_avg+"</td><td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
        

    //$("#body").html(htmlData); // 기존 html에 덮어씌워짐
    //$("#body").prepend(htmlData); // 기존 html 위쪽에 추가
    $("#body").append(htmlData); // 기존 html 뒤쪽에 추가
    
    // input 초기화
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
    $(".p_all").css("display","none");
   
    });// 학생입력

    // 전채 선택하기
    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            // 모든 체크박스 true
            console.log("전체선택됨");
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            });
        }else{ // 모든 체크박스 false
            console.log("전체해제됨");
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
        };
    }); // allChk

    $(document).on("click",".delBtn",function(){
        console.log("id : ",$(this).parent().parent().attr("id"));
        if(confirm("삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
            };
        });


    // table에 있는 삭제버튼 클릭
    // $(".delBtn").click(function(){
    //     console.log("id : ",$(this).parent().parent().attr("id"));
    //     if(confirm("삭제하시겠습니까?")){
    //         $("#"+$(this).parent().parent().attr("id")).remove();
    //     };
    // });

    // 하단 삭제버튼 클릭
    $("#deleteBtn").click(function(){
        console.log("체크박스 개수 : "+ $(".stuChk").length);
        console.log("체크박스에서 체크된 개수  : "+ $(".stuChk:checked").length);
        console.log("체크박스에서 체크된 개수  : "+ $("input:checkbox[name='stu']:checked").length);
        // 체크되어 있는게 없는 경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 항목을 선택하세요 !!!");
            return false;
        };
        // 현재 체크박스에 체크가 되어 있는지 확인
        if(!confirm("삭제하시겠습니까?")){
            return false; // no 누르면 다시 돌아감
        };
        
        // 모든 체크박스 가져오기
        $(".stuChk").each(function(){ // each() -> 배열, 객체확인 반복


            if($(this).is(":checked") == true){
                console.log("class 값 : "+$(this).val());
                console.log("id 값 : "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove();
            };
        }); // each       
    }); // 하단 삭제버튼

}); // jquery all