import React, { useState } from 'react'; //리액트 불러오기
import console from 'react-console'; //리액트 콘솔_크롬으로 실행
import './test.css';//test.css 불러오기

const Test3 = ( { history } ) =>
 {
	const questions_warm = [
		{
			questionText: '어두운 색상이 잘어울린다',
			answerOptions: [
				{ answerText: '예', isCorrect: false },
				{ answerText: '아니오', isCorrect: true }
			],
		},
		{
			questionText: '주변으로 부터 자주 듣는 나의 이미지는?',
			answerOptions: [
				{ answerText: '생기발랄', isCorrect: true },
				{ answerText: '지적이고, 성숙한', isCorrect: false }
			],
		},
		{
			questionText: '나는 동안 이미지이다',
			answerOptions: [
				{ answerText: '예', isCorrect: true },
				{ answerText: '아니오', isCorrect: false }
			],
		},
		{
			questionText: '진하고, 톤다운 된 색상이 잘어울린다',
			answerOptions: [
				{ answerText: '예', isCorrect: false },
				{ answerText: '아니오', isCorrect: true }
			],
		},
		{
			questionText: '피부가 투명하지만 얇아 주근깨가 많이 보인다',
			answerOptions: [
				{ answerText: '예', isCorrect: true },
				{ answerText: '아니오', isCorrect: false }
			],
		},
	]; //봄웜톤, 가을웜톤 파악


	const [currentQuestion_w, setCurrentQuestion] = useState(0); //현재 문제 번호 [변수, 함수]
	const [showScore_w, setShowScore] = useState(false); //결과 보여줄까?
	const [score_w_s, setScore_warm_spring] = useState(0);
	const [score_w_a, setScore_warm_autumn] = useState(0);
	const [score, setPersonal] = useState(""); //퍼스널컬러 결과
	const [num, setNum] = useState(0);
	

	const handleAnswerOptionClick = (isCorrect) => {  //main 함수 1_봄, 가을 검사
		if (isCorrect) {
			setScore_warm_spring(score_w_s+1);
		}
		else{
			setScore_warm_autumn(score_w_a+1);
		} ///봄, 가을 if문으로 점수 올리기

		const nextQuestion = currentQuestion_w + 1;
		if (nextQuestion < questions_warm.length) {
			setCurrentQuestion(nextQuestion);
		}
		else{
			setShowScore(true); //questions 끝나면 점수 보여줄까? true -> className='score-section'
		}
       
 }; //함수1 끝.

const handlePersonalScore_warm = (score_w_s,score_w_a) =>{ //함수2_봄, 가을 점수로 결과 구하기
	if(score_w_s>score_w_a){
		setPersonal('spring warm');
	}
	else if(score_w_s<score_w_a){
		setPersonal('autumn warm');
	}
	else{
		setPersonal('restart');
	}
	setNum(num + 1);
}; //함수2 끝.

	return (
		<div id='test'>
			<head>
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css"></link>
			</head>
			{showScore_w ? ( 
				<span className='score-section'>
					<button className="animated infinite pulse" id="result" onClick={() => handlePersonalScore_warm(score_w_s,score_w_a)}>result</button>
					{num === 1 ?
					(<div className = "season">
						{score === "spring warm" ? (<button id='next' onClick={ () => {history.push("/spring")}}>next</button>)
						: (<button id='next' onClick={ () => {history.push("/autumn")}}>next</button>)}
					</div>)
						: (<div className="animated infinite pulse">click me!</div>)}
				</span>
			) : (
				<>
				
					<div className='question-section'>
						<div id='question-count'>
							<span>Question {currentQuestion_w + 1}</span>/{questions_warm.length}
							<div className="animated infinite pulse">{questions_warm[currentQuestion_w].questionText}</div>
						</div>
					</div>
					<div className='answer-section'>
						{questions_warm[currentQuestion_w].answerOptions.map((answerOption) => (
							<button id = "btn_answer" onClick={() => handleAnswerOptionClick(answerOption.isCorrect)}>{answerOption.answerText}</button>
						))}
					</div>
				</>
			)}
		</div>
	);
}


export default Test3;