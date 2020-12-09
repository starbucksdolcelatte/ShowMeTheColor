import React, { useState } from 'react'; //리액트 불러오기
import console from 'react-console'; //리액트 콘솔_크롬으로 실행
import './test.css?v=1.0';//test.css 불러오기

const Test2 = ( { history } ) =>
 {
	const questions_cool = [
		{
			questionText: '파스텔 같이 은은한 색상보다 쨍한 색이 어울린다',
			answerOptions: [
				{ answerText: '예', isCorrect: false },
				{ answerText: '아니오', isCorrect: true }
			],
		},
		{
			questionText: '주변으로 부터 많이 듣는 나의 이미지는?',
			answerOptions: [
				{ answerText: '부드럽고, 맑은 느낌', isCorrect: true },
				{ answerText: '카리스마, 도시적인 느낌', isCorrect: false }
			],
		},
		{
			questionText: '전체적으로 강한 대비를 이루는 색상이 잘어울린다',
			answerOptions: [
				{ answerText: '예', isCorrect: false },
				{ answerText: '아니오', isCorrect: true }
			],
		},
		{
			questionText: '또렷하고, 선명한 색상이 잘어울린다',
			answerOptions: [
				{ answerText: '예', isCorrect: false },
				{ answerText: '아니오', isCorrect: true }
			],
		},
		{
			questionText: '회색기가 섞인 톤이 잘어울린다',
			answerOptions: [
				{ answerText: '예', isCorrect: true },
				{ answerText: '아니오', isCorrect: false }
			],
		},
	]; //여름쿨톤, 겨울쿨톤 파악

	const [currentQuestion_c, setCurrentQuestion] = useState(0); //현재 문제 번호 [변수, 함수]
	const [showScore_c, setShowScore] = useState(false); //결과 보여줄까?
	const [score_c_s, setScore_cool_summer] = useState(0);
	const [score_c_w, setScore_cool_winter] = useState(0);
	const [score, setPersonal] = useState(""); //퍼스널컬러 결과
	const [num, setNum] = useState(0);
	

	const handleAnswerOptionClick = (isCorrect) => {  //함수3_여쿨, 겨쿨 점수 +1
		if (isCorrect) {
			setScore_cool_summer(score_c_s + 1);
		}
		else{
			setScore_cool_winter(score_c_w + 1);
		} 

		const nextQuestion = currentQuestion_c + 1;
		if (nextQuestion < questions_cool.length) {
			setCurrentQuestion(nextQuestion);
		}
		else{
			setShowScore(true); //questions 끝나면 점수 보여줄까? true -> className='score-section'
		}
       
 }; //함수1 끝.

const handlePersonalScore_cool = (score_c_s,score_c_w) =>{ //함수2_여쿨, 겨쿨 점수로 결과 구하기
	if(score_c_s>score_c_w){
		setPersonal('summer cool');
	}
	else if(score_c_s<score_c_w){
		setPersonal('winter cool');
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
			{showScore_c ? ( 
				<span className='score-section'>
					<button className="animated infinite pulse" id="result" onClick={() => handlePersonalScore_cool(score_c_s,score_c_w)}>result</button>
					{num === 1 ?
					(<div className = "season">
						{score === "summer cool" ? (<button id='next' onClick={ () => {history.push("/summer")}}>next</button>)
						: (<button id='next' onClick={ () => {history.push("/winter")}}>next</button>)}
					</div>)
						: (<div>click me!</div>)}
				</span>
			) : (
				<>
				<div className='question-section'>
					<div id='question-count'>
						<span>Question{currentQuestion_c + 1}</span>/{questions_cool.length}
						<div className="animated infinite pulse">{questions_cool[currentQuestion_c].questionText}</div>
					</div>
				</div>
				<div className='answer-section'>
					{questions_cool[currentQuestion_c].answerOptions.map((answerOption) => (
						<button id = "btn_answer" onClick={() => handleAnswerOptionClick(answerOption.isCorrect)}>{answerOption.answerText}</button>
					))}
				</div>
				</>
			)}
		</div>
	);
}


export default Test2;