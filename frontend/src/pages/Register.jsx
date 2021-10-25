import React, { useState, useEffect } from 'react';
import styled, { css } from 'styled-components';
import { useHistory } from 'react-router-dom';

import { registerRequest } from 'apis/authApi';
import * as AuthForm from 'components/AuthForm';
import * as validation from "utils/validation";

const RegisterInputField = styled(AuthForm.InputField)`
    input {
        background-color: #F7F6F2;
        border: 2px solid ${props => props.valid ? "green" : "tomato"};
        ${props => props.value && css`
            border: 1px solid #4B6587;
        `}
    }
    input:focus {
        transform: scale(1.1);
    }
`

const Register = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [passwordCheck, setPasswordCheck] = useState("");
    const [name, setName] = useState("");
    const [isEmailValid, setIsEmailValid] = useState(false);
    const [isPasswordValid, setIsPasswordValid] = useState(false);
    const [isPasswordCheckValid, setIsPasswordCheckValid] = useState(false);
    const [isNameValid, setIsNameValid] = useState(false);
    const history = useHistory();

    const handleRegisterSubmit = e => {
        e.preventDefault();
        (async () => {
            try {
                await registerRequest(email, password, name);
                alert("회원가입에 성공하였습니다. 로그인 화면으로 이동합니다.");
                history.push("/");
            } catch (e) {
                alert(e.response.data.message);
            }
        })();
    }

    useEffect(() => {
        setIsEmailValid(validation.emailValidation(email));
    }, [email]);

    useEffect(() => {
        setIsPasswordValid(validation.passwordValidation(password));
        setIsPasswordCheckValid(validation.passwordCheckValidation(password, passwordCheck));
    }, [password, passwordCheck]);

    useEffect(() => {
        setIsNameValid(validation.nameValidation(name));
    }, [name]);

    return (
        <AuthForm.FormWrapper>
            <AuthForm.Form onSubmit={handleRegisterSubmit}>
                <RegisterInputField valid={isEmailValid} value={email === ""}>
                    <label htmlFor="email">아이디</label>
                    <input type="text" id="email" name="email" placeholder="email" value={email} onChange={e => setEmail(e.target.value)} />
                </RegisterInputField >
                {(email !== "" && !isEmailValid) && <AuthForm.WarningMessage>올바른 이메일 형식이 아닙니다.</AuthForm.WarningMessage>}
                <RegisterInputField valid={isPasswordValid} value={password === ""}>
                    <label htmlFor="password">비밀번호</label>
                    <input type="password" autoComplete="off" id="password" name="password" placeholder="password" value={password} onChange={e => setPassword(e.target.value)} />
                </RegisterInputField>
                {(password !== "" && !isPasswordValid) && <AuthForm.WarningMessage>비밀번호는 8자리 이상의 영문+숫자+특수문자 혹은,<br />10자리 이상의 영문+숫자의 조합이어야합니다.</AuthForm.WarningMessage>}
                <RegisterInputField valid={isPasswordCheckValid} value={passwordCheck === ""}>
                    <label htmlFor="password_check">비밀번호 확인</label>
                    <input type="password" autoComplete="off" id="password_check" name="password_check" placeholder="password_check" value={passwordCheck} onChange={e => setPasswordCheck(e.target.value)} />
                </RegisterInputField>
                {(passwordCheck !== "" && !isPasswordCheckValid) && <AuthForm.WarningMessage>비밀번호 확인이 일치하지 않습니다.</AuthForm.WarningMessage>}
                <RegisterInputField valid={isNameValid} value={name === ""}>
                    <label htmlFor="email">이름</label>
                    <input type="text" id="name" name="name" placeholder="name" value={name} onChange={e => setName(e.target.value)} />
                </RegisterInputField>
                {(name !== "" && !isNameValid) && <AuthForm.WarningMessage>이름은 영문이나 한글로 입력해주세요.</AuthForm.WarningMessage>}
                <button type="submit" disabled={!isEmailValid || !isPasswordValid || !isPasswordCheckValid || !isNameValid}>가입하기</button>
                <button type="button" onClick={() => history.push("/login")}>로그인 화면으로</button>
            </AuthForm.Form>
        </AuthForm.FormWrapper>
    );
};

export default Register;