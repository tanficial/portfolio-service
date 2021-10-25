import styled from "styled-components"

export const PortfolioCardWrapper = styled.div`
    position: relative;
    background-color: #C8C6C6;
    border-radius: 5px;
    padding: 40px;
    padding-bottom: 80px;
    color: #222831;

    > h2 {
        color: #222831;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 20px;
    }
    & + & {
        margin-top: 20px;
    }
`

export const PortfolioElement = styled.div`
    padding: 30px 10px;
    border-top: 2px solid rgba(75, 101, 135, 0.4);
    * + * {
        margin-top: 10px;
    }

    > P:first-child {
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 15px;
    }
    span {
        opacity: 0.8;
        font-size: 14px;
    }
    > span {
        display: inline-block;
        margin-top: 8px;
    }
`

export const ButtonWrapper = styled.div`
    position: absolute;
    bottom: 40px;
    right: 40px;
    * + * {
        margin-left: 8px;
    }
`

export const Button = styled.button`
    border: none;
    box-sizing: border-box;
    background-color: #4B6587;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    padding: 4px 8px;
    color: white;

    :hover {
        transform: scale(1.1);
    }

`